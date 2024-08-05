# 함수 구현 - 섭씨(C) -> 화씨(F) 온도 변환
## 사용자로부터 섭씨 온도를 입력받아 화씨 온도로 변환하는 함수를 작성하고, 변환된 화씨 온도를 출력하는 프로그램
## 화씨 온도는 섭씨 온도에 9/5를 곱한 후 32를 더해 계산합니다
## F = (C * 9/5) + 32


# 1. 블릿 2: 섭씨를 화씨로 변환하는 함수를 작성합니다.

def convert_celsius_to_fahrenheit(celsius): ## 온도 변환 함수
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# 2. 사용자에게 섭씨 온도를 입력 받습니다.

user_celsius = int(input("섭씨 온도를 입력하세요: "))

# 3. 블릿 3: 변환된 화씨 온도를 출력합니다.

print("화씨 온도는", convert_celsius_to_fahrenheit(user_celsius), end="입니다.")





#################################################


# 혼자 처음 한 것.

# # 1. 사용자에게 섭씨 온도를 입력 받습니다.

# celsius = int(input("섭씨 온도를 입력하세요: "))

# # 2. 블릿 2: 섭씨를 화씨로 변환하는 함수를 작성합니다.

# def convert_celsius_to_fahrenheit(celsius): ## 온도 변환 함수
#     return (celsius * 9 / 5) +32

# # 3. 블릿 3: 변환된 화씨 온도를 출력합니다.

# print("화씨 온도는", convert_celsius_to_fahrenheit(celsius), end="입니다.")