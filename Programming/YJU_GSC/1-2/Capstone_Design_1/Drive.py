import Jetson.GPIO as GPIO
import time
import keyboard
import subprocess

# sudo 비밀번호를 변수로 설정하여 쉽게 업데이트할 수 있도록 함
sudo_password = "12"

# sudo 비밀번호를 사용하여 쉘 명령을 실행하는 함수
def run_command(command):
    # 비밀번호 입력을 포함한 전체 명령어 구성
    full_command = f"echo {sudo_password} | sudo -S {command}"
    # 쉘에서 명령 실행
    subprocess.run(full_command, shell=True, check=True)

# busybox가 설치되었는지 확인하고, 설치되지 않은 경우 설치
try:
    subprocess.run("busybox --help", shell=True, check=True)
    print("busybox가 이미 설치되어 있습니다.")
except subprocess.CalledProcessError:
    print("busybox를 찾을 수 없습니다. 설치 중...")
    run_command("apt update && apt install -y busybox")

# devmem 명령 정의
commands = [
    "busybox devmem 0x700031fc 32 0x45",
    "busybox devmem 0x6000d504 32 0x2",
    "busybox devmem 0x70003248 32 0x46",
    "busybox devmem 0x6000d100 32 0x00"
]

# 각 devmem 명령 실행
for command in commands:
    run_command(command)

# 서보 및 DC 모터 제어를 위한 GPIO 핀 설정
servo_pin = 33  # 서보 모터용 PWM 핀
dc_motor_pwm_pin = 32  # DC 모터 속도용 PWM 핀
dc_motor_dir_pin1 = 29  # 방향 제어 핀 1
dc_motor_dir_pin2 = 31  # 방향 제어 핀 2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(dc_motor_pwm_pin, GPIO.OUT)
GPIO.setup(dc_motor_dir_pin1, GPIO.OUT)
GPIO.setup(dc_motor_dir_pin2, GPIO.OUT)

# 서보 및 DC 모터 핀에 PWM 설정
servo = GPIO.PWM(servo_pin, 50)  # 서보 모터용 50Hz PWM
dc_motor_pwm = GPIO.PWM(dc_motor_pwm_pin, 1000)  # DC 모터용 1kHz PWM
servo.start(0)
dc_motor_pwm.start(0)

# 서보 각도 설정 함수
def set_servo_angle(angle):
    # 각도(0~180도)에 따른 듀티 사이클 계산
    duty_cycle = 2 + (angle / 18)
    servo.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # 서보가 위치에 도달할 시간 대기
    servo.ChangeDutyCycle(0)  # 신호를 꺼서 떨림 방지

# DC 모터 속도 및 방향 설정 함수
def set_dc_motor(speed, direction):
    # 방향 설정: 'forward'(전진) 또는 'backward'(후진)
    if direction == "forward":
        GPIO.output(dc_motor_dir_pin1, GPIO.HIGH)
        GPIO.output(dc_motor_dir_pin2, GPIO.LOW)
    elif direction == "backward":
        GPIO.output(dc_motor_dir_pin1, GPIO.LOW)
        GPIO.output(dc_motor_dir_pin2, GPIO.HIGH)
    
    # PWM으로 속도 제어(0~100%)
    dc_motor_pwm.ChangeDutyCycle(speed)

# 예제 사용법: W, A, S, D 키로 서보 및 DC 모터 제어
try:
    current_servo_angle = 90  # 초기 각도를 중간 위치로 설정
    set_servo_angle(current_servo_angle)

    print("W, A, S, D 키로 서보 및 모터를 제어하세요. 'q'를 눌러 종료합니다.")
    while True:
        if keyboard.is_pressed('w'):
            print("W 키 눌림: DC 모터 전진")
            set_dc_motor(50, "forward")
        elif keyboard.is_pressed('s'):
            print("S 키 눌림: DC 모터 후진")
            set_dc_motor(50, "backward")
        elif keyboard.is_pressed('a'):
            print("A 키 눌림: 서보 왼쪽")
            current_servo_angle = max(0, current_servo_angle - 10)
            set_servo_angle(current_servo_angle)
        elif keyboard.is_pressed('d'):
            print("D 키 눌림: 서보 오른쪽")
            current_servo_angle = min(180, current_servo_angle + 10)
            set_servo_angle(current_servo_angle)
        elif keyboard.is_pressed('q'):
            print("종료 키 눌림")
            break
        else:
            set_dc_motor(0, "forward")  # 키가 눌리지 않으면 모터 정지

        time.sleep(0.1)  # CPU 사용량을 줄이기 위한 짧은 지연 시간

finally:
    # 모든 PWM 정지 및 GPIO 정리
    servo.stop()
    dc_motor_pwm.stop()
    GPIO.cleanup()
