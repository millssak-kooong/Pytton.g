import threading
import cv2
import datetime
import Jetson.GPIO as GPIO
import time
import keyboard
import os
import numpy as np

# 방향별 저장 경로 설정
base_directory = "/home/gsc2423020/다운로드/Dataset"
save_directories = {
    "left": os.path.join(base_directory, "Left"),
    "center": os.path.join(base_directory, "Center"),
    "right": os.path.join(base_directory, "Right"),
}

# 폴더 생성
for directory in save_directories.values():
    os.makedirs(directory, exist_ok=True)

# 카메라 영상 처리 함수
def camera_processing():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("카메라를 열 수 없습니다")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("실시간 영상이 시작됩니다. 방향에 따라 이미지 저장 중입니다.")
    print("'q' 키를 누르면 종료됩니다.")

    interval = 0.1  # 이미지 저장 간격 (초)
    next_capture_time = time.time()

    def detect_line_direction(frame):
        """ 흰색 라인을 감지하고 중심 좌표를 계산해 방향을 반환 """
        height, width = frame.shape[:2]
        roi = frame[height // 2:, :]  # 화면 하단 절반만 관심 영역으로 설정

        # 1. HSV 색상 필터링: 흰색 검출
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        lower_white = np.array([0, 0, 200], dtype=np.uint8)
        upper_white = np.array([180, 30, 255], dtype=np.uint8)
        mask_white = cv2.inRange(hsv, lower_white, upper_white)

        # 2. 엣지 검출 및 중심 좌표 계산
        edges = cv2.Canny(mask_white, 50, 150)

        # OpenCV 버전 호환성 처리
        version = cv2.__version__.split(".")[0]
        if int(version) >= 4:  # OpenCV 4.x
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        else:  # OpenCV 2.x 및 이전
            _, contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])  # 라인의 중심 X 좌표
                center_threshold = width // 3  # 화면을 3등분
                if cx < center_threshold:
                    return "left"
                elif cx > 2 * center_threshold:
                    return "right"
                else:
                    return "center"  # "Straight" 대신 "Center"로 저장
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("영상을 가져올 수 없습니다.")
            break

        current_time = time.time()
        if current_time >= next_capture_time:
            direction = detect_line_direction(frame)  # 라인 방향 감지
            if direction:
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3]
                filename = os.path.join(save_directories[direction], f"{direction}_{timestamp}.jpg")
                cv2.imwrite(filename, frame)
                print(f"[{direction.upper()}] 방향 사진 저장: {filename}")
            else:
                print("라인을 감지하지 못했습니다.")

            next_capture_time = current_time + interval

        # 화면 출력
        cv2.imshow("Line Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("종료합니다.")
            break

    cap.release()
    cv2.destroyAllWindows()

# 모터 제어 함수 (원래 코드 유지)
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
        time.sleep(0.05)

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
                set_dc_motor(50, "forward")
            elif keyboard.is_pressed('s'):
                set_dc_motor(50, "backward")
            else:
                set_dc_motor(0, "forward")

            if keyboard.is_pressed('a'):
                target_angle = max(15, current_servo_angle - 5)
                current_servo_angle = target_angle
                set_servo_angle(current_servo_angle)
            elif keyboard.is_pressed('d'):
                target_angle = min(165, current_servo_angle + 5)
                current_servo_angle = target_angle
                set_servo_angle(current_servo_angle)

            if keyboard.is_pressed('q'):
                break

            time.sleep(0.1)
    finally:
        servo.stop()
        dc_motor_pwm.stop()
        GPIO.cleanup()

# 멀티 스레드로 실행
camera_thread = threading.Thread(target=camera_processing)
motor_thread = threading.Thread(target=motor_control)

camera_thread.start()
motor_thread.start()

camera_thread.join()
motor_thread.join()
