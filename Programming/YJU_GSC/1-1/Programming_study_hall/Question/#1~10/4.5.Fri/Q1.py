# 평균 속도 계산기
## 차량이 어떤 거리를 이동하는 데 걸린 시간과 이동 거리를 바탕으로 평균 속도를 계산하는 프로그램을 작성
## 작성자로부터 출발 시간과 도착 시간(시와 분 별도 입력), 그리고 이동 거리를 입력받습니다.
## 평균 속도를 km/h 단위로 계산하고 그 속도가 "느림", "보통", 또는 "빠름" 중 어느 것에 해당하는지 출력
### 입력 1. 출발 시간(시), 2. 출발 시간(분), 3. 도착 시간(시), 4. 도착 시간(분), 5. 이동 거리(km)
### 출력 1. 이동 거리, 2. 출발 시간, 3. 도착 시간, 4. 평균 속도(km/h), 5. 속도 상태("느림", "보통", "빠름")
#### 평균 속도 = 이동 거리(km) / 총 이동 시간(h)
#### 총 이동 시간은 분 단위로 환산하여 계산합니다.
#### 평균 속도가 60km/h 미만이면 속도 상태를 "느림"으로, 60km/h 이상 90km/h 미만이면 "보통"으로, 90km/h 이상이면 "빠름"으로 분류

# 1. 입력 값들을 받아낸다.

departure_hour = int(input("출발 시간의 '시'를 입력하시오.: "))
departure_min = int(input("출발 시간의 '분'를 입력하시오.: "))
arrival_hour = int(input("도착 시간의 '시'를 입력하시오.: "))
arrival_min = int(input("도착 시간의 '분'를 입력하시오.: "))
distance = int(input("이동 거리(km)를 입력하시오.: "))    

# 2. 단순 출력값들 출력

print(f"이동 거리: {float(distance)}km")
print(f"출발 시간: {departure_hour}시 {departure_min}분")
print(f"도착 시간: {arrival_hour}시 {arrival_min}분")

# 3. 평균 속도를 계산하고 출력

average_speed = distance / (arrival_hour - departure_hour + (arrival_min - departure_min) / 60)
print(f"평균 속도: {round(float(average_speed), 2)}km/h")

# 4. 속도 상태 구분하여 출력

speed_level = ""

if average_speed < 60:
    speed_level = "느림"
elif 60 <= average_speed < 90:
    speed_level = "보통"
else:
    speed_level = "빠름"

print(f"속도 상태: {speed_level}")