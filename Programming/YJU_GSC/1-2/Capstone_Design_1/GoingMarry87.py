import threading  # 스레드 처리를 위한 라이브러리
import cv2  # OpenCV 라이브러리를 사용하여 영상 처리
import datetime  # 타임스탬프 생성용
import Jetson.GPIO as GPIO  # Jetson Nano의 GPIO 핀 제어를 위한 라이브러리
import time  # 딜레이 처리를 위한 라이브러리
import keyboard  # 키보드 입력 감지를 위한 라이브러리
import os  # 파일 경로 관리를 위한 라이브러리

# 카메라 영상 처리를 위한 함수
def camera_processing():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("카메라를 열 수 없습니다")
        return

    save_directory = "/home/gsc2423020/다운로드/Dataset"  # 저장할 경로 설정
    os.makedirs(save_directory, exist_ok=True)  # 폴더가 없으면 생성

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("실시간 영상이 시작됩니다.")
    print("1초에 10장의 사진을 자동으로 촬영합니다.")
    print("'t' 키를 눌러 촬영을 시작/중지할 수 있습니다.")
    print("'q' 키를 누르면 종료됩니다.")

    capturing = False  # 촬영 상태를 나타내는 변수
    interval = 0.1  # 사진 촬영 간격 (초)
    next_capture_time = time.time()  # 다음 사진 촬영 시간 초기화

    while True:
        ret, frame = cap.read()
        if not ret:
            print("영상을 가져올 수 없습니다")
            break

        current_time = time.time()

        # 촬영이 활성화된 경우에만 사진 저장
        if capturing and current_time >= next_capture_time:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3]  # 밀리초까지 저장
            filename = f"{save_directory}/photo_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"사진이 저장되었습니다: {filename}")
            next_capture_time += interval  # 다음 촬영 시간을 업데이트

        cv2.imshow('Live Feed', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("종료합니다.")
            break
        elif key == ord('t'):
            capturing = not capturing  # 촬영 상태 전환
            if capturing:
                print("촬영 시작")
                next_capture_time = time.time()  # 현재 시간으로 초기화
            else:
                print("촬영 중지")

    cap.release()
    cv2.destroyAllWindows()

# 모터 제어를 위한 함수
def motor_control():
    servo_pin = 33
    dc_motor_pwm_pin = 32
    dc_motor_dir_pin1 = 29
    dc_motor_dir_pin2 = 31

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servo_pin, GPIO.OUT)
    GPIO.setup(dc_motor_pwm_pin, GPIO.OUT)
    GPIO.setup(dc_motor_dir_pin1, GPIO.OUT)
    GPIO.setup(dc_motor_dir_pin2, GPIO.OUT)

    servo = GPIO.PWM(servo_pin, 50)
    dc_motor_pwm = GPIO.PWM(dc_motor_pwm_pin, 1000)
    servo.start(0)
    dc_motor_pwm.start(0)

    def set_servo_angle(angle):
        duty_cycle = 2 + (angle / 18)
        servo.ChangeDutyCycle(duty_cycle)
        time.sleep(0.05)  # 응답 속도를 줄여 부드럽게 조향

    def set_dc_motor(speed, direction):
        if direction == "forward":
            GPIO.output(dc_motor_dir_pin1, GPIO.HIGH)
            GPIO.output(dc_motor_dir_pin2, GPIO.LOW)
        elif direction == "backward":
            GPIO.output(dc_motor_dir_pin1, GPIO.LOW)
            GPIO.output(dc_motor_dir_pin2, GPIO.HIGH)
        dc_motor_pwm.ChangeDutyCycle(speed)

    try:
        current_servo_angle = 90
        set_servo_angle(current_servo_angle)

        print("W: 전진, S: 후진, A: 좌회전, D: 우회전, Q: 종료")

        while True:
            if keyboard.is_pressed('w'):
                print("전진 중")
                set_dc_motor(50, "forward")
            elif keyboard.is_pressed('s'):
                print("후진 중")
                set_dc_motor(50, "backward")
            else:
                set_dc_motor(0, "forward")

            if keyboard.is_pressed('a'):
                print("좌회전 중")
                target_angle = max(15, current_servo_angle - 5)  # 좌측 방향으로 5도씩 변경
                current_servo_angle = target_angle
                set_servo_angle(current_servo_angle)
            elif keyboard.is_pressed('d'):
                print("우회전 중")
                target_angle = min(165, current_servo_angle + 5)  # 우측 방향으로 5도씩 변경
                current_servo_angle = target_angle
                set_servo_angle(current_servo_angle)

            if keyboard.is_pressed('q'):
                print("프로그램 종료")
                break

            time.sleep(0.1)
    finally:
        print("모터와 GPIO 정리 중")
        servo.stop()
        dc_motor_pwm.stop()
        GPIO.cleanup()

camera_thread = threading.Thread(target=camera_processing)
motor_thread = threading.Thread(target=motor_control)

camera_thread.start()
motor_thread.start()

camera_thread.join()
motor_thread.join()
