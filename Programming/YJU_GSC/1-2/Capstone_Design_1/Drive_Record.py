import threading
import cv2
import datetime
import Jetson.GPIO as GPIO
import time
import keyboard
import subprocess

# 카메라 영상 처리를 위한 함수
def camera_processing():
    # 카메라 초기화 (카메라 디바이스가 여러 개 있는 경우 번호 변경)
    cap = cv2.VideoCapture(0)  # 0은 기본 카메라를 지정

    if not cap.isOpened():  # 카메라를 열 수 없는 경우 오류 처리
        print("카메라를 열 수 없습니다.")
        return

    # 카메라 해상도 설정 (640x480 픽셀)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 동영상 저장을 위한 설정
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # XVID 코덱 사용
    out = None  # 녹화를 위한 VideoWriter 객체 (초기 값 None)
    recording = False  # 녹화 상태를 관리하는 플래그

    print("실시간 영상이 시작됩니다.")
    print("'r' 키를 눌러 녹화를 시작하세요.")
    print("'r' 키를 다시 눌러 녹화를 중지하세요.")
    print("'q' 키를 눌러 종료하세요.")

    while True:
        # 카메라에서 프레임 가져오기
        ret, frame = cap.read()
        if not ret:  # 영상을 가져오지 못한 경우 오류 처리
            print("영상을 가져올 수 없습니다.")
            break

        # 프레임을 창에 표시
        cv2.imshow('Live Feed', frame)

        # 녹화 중인 경우 현재 프레임을 동영상 파일에 기록
        if recording and out is not None:
            out.write(frame)

        # 키보드 입력 처리
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # 'q' 키로 종료
            print("종료합니다.")
            if recording:  # 녹화 중이면 녹화를 중지
                recording = False
                out.release()
                print("녹화를 중지했습니다.")
            break
        elif key == ord('r'):  # 'r' 키로 녹화 시작/중지 전환
            if not recording:  # 녹화가 중지 상태인 경우
                # 타임스탬프를 사용해 파일명 생성
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f"recording_{timestamp}.avi"
                out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))  # 새로운 동영상 파일 생성
                recording = True
                print(f"녹화를 시작했습니다: {filename}")
            else:  # 녹화 중인 경우
                recording = False
                out.release()  # 현재 동영상 파일 닫기
                print("녹화를 중지했습니다.")

    # 카메라와 리소스 해제
    cap.release()
    if out is not None:
        out.release()  # VideoWriter 리소스 해제
    cv2.destroyAllWindows()  # OpenCV의 모든 창 닫기

# 모터 제어를 위한 함수
def motor_control():
    # Sudo 권한으로 명령 실행을 위한 비밀번호 (안전성을 위해 실제 운영에서는 외부에서 읽어야 함)
    sudo_password = " "

    # 서브프로세스로 명령 실행을 위한 헬퍼 함수
    def run_command(command):
        full_command = f"echo {sudo_password} | sudo -S {command}"  # sudo 명령 실행
        subprocess.run(full_command, shell=True, check=True)

    # 필요한 도구 (busybox)가 설치되어 있는지 확인하고 설치
    try:
        subprocess.run("busybox --help", shell=True, check=True)
    except subprocess.CalledProcessError:  # busybox가 없는 경우
        run_command("apt update && apt install -y busybox")  # busybox 설치

    # 특정 레지스터에 데이터를 기록하는 명령 (모터 제어 준비)
    commands = [
        "busybox devmem 0x700031fc 32 0x45",
        "busybox devmem 0x6000d504 32 0x2",
        "busybox devmem 0x70003248 32 0x46",
        "busybox devmem 0x6000d100 32 0x00"
    ]
    for command in commands:
        run_command(command)

    # GPIO 핀 설정
    servo_pin = 33  # 서보 모터 제어용 핀
    dc_motor_pwm_pin = 32  # DC 모터 속도 제어용 PWM 핀
    dc_motor_dir_pin1 = 29  # DC 모터 방향 제어 핀 1
    dc_motor_dir_pin2 = 31  # DC 모터 방향 제어 핀 2

    # GPIO 모드 설정
    GPIO.setmode(GPIO.BOARD)  # 핀 번호 기준 BOARD 모드 사용
    GPIO.setup(servo_pin, GPIO.OUT)  # 서보 모터 핀 출력 설정
    GPIO.setup(dc_motor_pwm_pin, GPIO.OUT)  # DC 모터 PWM 핀 출력 설정
    GPIO.setup(dc_motor_dir_pin1, GPIO.OUT)  # DC 모터 방향 핀 1 출력 설정
    GPIO.setup(dc_motor_dir_pin2, GPIO.OUT)  # DC 모터 방향 핀 2 출력 설정

    # PWM 신호 생성
    servo = GPIO.PWM(servo_pin, 50)  # 서보 모터 (50Hz로 제어)
    dc_motor_pwm = GPIO.PWM(dc_motor_pwm_pin, 1000)  # DC 모터 (1000Hz로 제어)
    servo.start(0)  # 초기 듀티 사이클을 0으로 설정
    dc_motor_pwm.start(0)  # 초기 듀티 사이클을 0으로 설정

    # 서보 모터 각도를 설정하는 함수
    def set_servo_angle(angle):
        duty_cycle = 2 + (angle / 18)  # 각도를 듀티 사이클로 변환
        servo.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)  # 모터가 움직이는 동안 대기
        servo.ChangeDutyCycle(0)  # 신호 정지

    # DC 모터 속도와 방향을 설정하는 함수
    def set_dc_motor(speed, direction):
        if direction == "forward":  # 전진인 경우
            GPIO.output(dc_motor_dir_pin1, GPIO.HIGH)
            GPIO.output(dc_motor_dir_pin2, GPIO.LOW)
        elif direction == "backward":  # 후진인 경우
            GPIO.output(dc_motor_dir_pin1, GPIO.LOW)
            GPIO.output(dc_motor_dir_pin2, GPIO.HIGH)
        dc_motor_pwm.ChangeDutyCycle(speed)  # 듀티 사이클로 속도 조정

    try:
        current_servo_angle = 90  # 서보 모터 초기 각도를 90도로 설정
        set_servo_angle(current_servo_angle)  # 초기 위치로 이동

        print("W, A, S, D 키로 모터를 조작합니다. 종료하려면 'q' 키를 누르세요.")
        while True:
            # 키보드 입력에 따라 모터 제어
            if keyboard.is_pressed('w'):  # 'W' 키로 전진
                print("W 키 눌림: 전진")
                set_dc_motor(70, "forward")
            elif keyboard.is_pressed('s'):  # 'S' 키로 후진
                print("S 키 눌림: 후진")
                set_dc_motor(70, "backward")
            elif keyboard.is_pressed('a'):  # 'A' 키로 좌회전
                print("A 키 눌림: 서보 좌회전")
                current_servo_angle = max(0, current_servo_angle - 10)  # 각도를 10도 감소
                set_servo_angle(current_servo_angle)
            elif keyboard.is_pressed('d'):  # 'D' 키로 우회전
                print("D 키 눌림: 서보 우회전")
                current_servo_angle = min(180, current_servo_angle + 10)  # 각도를 10도 증가
                set_servo_angle(current_servo_angle)
            elif keyboard.is_pressed('q'):  # 'Q' 키로 종료
                print("종료합니다.")
                break
            else:
                # 입력이 없는 경우 모터 정지
                set_dc_motor(0, "forward")

            time.sleep(0.1)  # 키보드 입력 판정을 반복하는 간격
    finally:
        # 종료 시 모든 리소스를 해제
        servo.stop()  # 서보 모터 PWM 신호 정지
        dc_motor_pwm.stop()  # DC 모터 PWM 신호 정지
        GPIO.cleanup()  # GPIO 핀 해제

# 스레드 정의 및 시작
camera_thread = threading.Thread(target=camera_processing)  # 카메라 처리 스레드
motor_thread = threading.Thread(target=motor_control)  # 모터 제어 스레드

camera_thread.start()  # 카메라 처리 시작
motor_thread.start()  # 모터 제어 시작

# 스레드가 종료될 때까지 대기
camera_thread.join()
motor_thread.join()
