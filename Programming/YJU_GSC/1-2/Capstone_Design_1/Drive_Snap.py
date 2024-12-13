import threading  # 스레드 처리를 위한 라이브러리
import cv2  # OpenCV 라이브러리를 사용하여 영상 처리
import datetime  # 타임스탬프 생성용
import Jetson.GPIO as GPIO  # Jetson Nano의 GPIO 핀 제어를 위한 라이브러리
import time  # 딜레이 처리를 위한 라이브러리
import keyboard  # 키보드 입력 감지를 위한 라이브러리

# 카메라 영상 처리를 위한 함수
def camera_processing():
    # 카메라 초기화 (기본 카메라 사용 시 0을 인수로 설정)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("카메라를 열 수 없습니다")  # 카메라 사용 불가 시 오류 메시지
        return

    # 카메라 해상도 설정
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 가로 해상도를 640픽셀로 설정
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 세로 해상도를 480픽셀로 설정

    print("실시간 영상이 시작됩니다.")
    print("'p' 키를 누르면 사진을 촬영합니다.")
    print("'q' 키를 누르면 종료됩니다.")

    while True:
        # 카메라에서 프레임 1개를 가져옴
        ret, frame = cap.read()
        if not ret:
            print("영상을 가져올 수 없습니다")  # 프레임을 가져오지 못한 경우
            break

        # 프레임을 화면에 표시
        cv2.imshow('Live Feed', frame)

        # 키보드 입력 감지
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # 'q' 키를 누르면 종료
            print("종료합니다.")
            break
        elif key == ord('p'):  # 'p' 키를 누르면 사진 촬영
            # 타임스탬프를 사용하여 고유한 파일명 생성
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            filename = f"photo_{timestamp}.jpg"
            cv2.imwrite(filename, frame)  # 프레임을 JPEG 이미지로 저장
            print(f"사진이 저장되었습니다: {filename}")

    # 카메라와 창 해제
    cap.release()
    cv2.destroyAllWindows()

# 모터 제어를 위한 함수
def motor_control():
    # GPIO 핀 번호 정의 (BOARD 모드 사용)
    servo_pin = 33  # 서보 모터 제어용 핀 번호
    dc_motor_pwm_pin = 32  # DC 모터의 PWM 제어용 핀 번호
    dc_motor_dir_pin1 = 29  # DC 모터의 방향 제어 핀 1
    dc_motor_dir_pin2 = 31  # DC 모터의 방향 제어 핀 2

    # GPIO 모드 설정
    GPIO.setmode(GPIO.BOARD)  # BOARD 모드(물리적인 핀 번호)를 사용
    GPIO.setup(servo_pin, GPIO.OUT)  # 서보 모터 핀을 출력 모드로 설정
    GPIO.setup(dc_motor_pwm_pin, GPIO.OUT)  # PWM 핀을 출력 모드로 설정
    GPIO.setup(dc_motor_dir_pin1, GPIO.OUT)  # 방향 제어 핀 1을 출력 모드로 설정
    GPIO.setup(dc_motor_dir_pin2, GPIO.OUT)  # 방향 제어 핀 2를 출력 모드로 설정

    # PWM 신호 초기화
    servo = GPIO.PWM(servo_pin, 50)  # 서보 모터용 PWM, 50Hz(20ms 주기)
    dc_motor_pwm = GPIO.PWM(dc_motor_pwm_pin, 1000)  # DC 모터용 PWM, 1000Hz
    servo.start(0)  # 서보 모터의 PWM을 0% 듀티로 시작 (초기화)
    dc_motor_pwm.start(0)  # DC 모터의 PWM을 0% 듀티로 시작 (초기화)

    # 서보 모터 각도를 설정하는 함수
    def set_servo_angle(angle):
        """
        서보 모터를 지정된 각도로 회전시키는 함수.
        :param angle: 서보 모터 목표 각도 (0~180도)
        """
        # 각도를 듀티 사이클(2~12%)로 변환
        duty_cycle = 2 + (angle / 18)  # 데이터시트에 기반한 변환식
        servo.ChangeDutyCycle(duty_cycle)  # PWM 듀티 사이클 설정
        time.sleep(0.1)  # 짧은 딜레이 추가로 서보 모터 동작 안정화
        servo.ChangeDutyCycle(0)  # 정지 신호를 전송하여 각도를 유지

    # DC 모터의 속도와 방향을 설정하는 함수
    def set_dc_motor(speed, direction):
        """
        DC 모터의 동작을 제어하는 함수.
        :param speed: 모터 속도 (0~100%)
        :param direction: 모터 회전 방향 ("forward" 또는 "backward")
        """
        if direction == "forward":
            # 전진 방향: 핀 1을 HIGH, 핀 2를 LOW로 설정
            GPIO.output(dc_motor_dir_pin1, GPIO.HIGH)
            GPIO.output(dc_motor_dir_pin2, GPIO.LOW)
        elif direction == "backward":
            # 후진 방향: 핀 1을 LOW, 핀 2를 HIGH로 설정
            GPIO.output(dc_motor_dir_pin1, GPIO.LOW)
            GPIO.output(dc_motor_dir_pin2, GPIO.HIGH)
        # PWM 듀티 사이클을 설정하여 속도 제어
        dc_motor_pwm.ChangeDutyCycle(speed)

    try:
        # 초기 상태: 서보 모터를 90도(중앙 위치)로 설정
        current_servo_angle = 90
        set_servo_angle(current_servo_angle)  # 서보 모터를 중앙에 배치
        motor_running = False  # 모터가 작동 중인지 여부를 나타내는 플래그

        print("W 키를 누르면 DC 모터가 전진합니다.")
        print("S 키를 누르면 모터가 정지합니다.")
        print("A 키를 누르면 서보 모터가 왼쪽으로 회전합니다.")
        print("D 키를 누르면 서보 모터가 오른쪽으로 회전합니다.")
        print("Q 키를 누르면 종료합니다.")

        while True:
            if keyboard.is_pressed('w') and not motor_running:
                print("W 키가 눌렸습니다: DC 모터가 전진합니다.")
                set_dc_motor(50, "forward")  # 전진 속도 50%로 모터 작동
                motor_running = True  # 모터가 작동 중임을 설정
            elif keyboard.is_pressed('s'):
                print("S 키가 눌렸습니다: DC 모터가 정지합니다.")
                set_dc_motor(0, "forward")  # 모터 정지 (속도 0%)
                motor_running = False  # 모터를 정지 상태로 설정
            elif keyboard.is_pressed('a'):
                print("A 키가 눌렸습니다: 서보 모터가 왼쪽으로 회전합니다.")
                current_servo_angle = max(0, current_servo_angle - 10)  # 왼쪽 회전 (각도 감소)
                set_servo_angle(current_servo_angle)
            elif keyboard.is_pressed('d'):
                print("D 키가 눌렸습니다: 서보 모터가 오른쪽으로 회전합니다.")
                current_servo_angle = min(180, current_servo_angle + 10)  # 오른쪽 회전 (각도 증가)
                set_servo_angle(current_servo_angle)
            elif keyboard.is_pressed('q'):  # 'q' 키를 누르면 루프 종료
                print("Q 키가 눌렸습니다: 프로그램을 종료합니다.")
                break

            time.sleep(0.1)  # 입력 감지 간격을 짧은 딜레이로 설정
    finally:
        # 모터를 안전하게 정지하고 GPIO 해제
        print("모터와 GPIO를 정리합니다.")
        servo.stop()  # 서보 모터의 PWM 정지
        dc_motor_pwm.stop()  # DC 모터의 PWM 정지
        GPIO.cleanup()  # GPIO 리소스를 해제하여 정리

# 카메라와 모터 제어를 병렬로 실행할 스레드 생성
camera_thread = threading.Thread(target=camera_processing)
motor_thread = threading.Thread(target=motor_control)

# 병렬 처리 시작
camera_thread.start()
motor_thread.start()

# 스레드 종료 대기
camera_thread.join()
motor_thread.join()
