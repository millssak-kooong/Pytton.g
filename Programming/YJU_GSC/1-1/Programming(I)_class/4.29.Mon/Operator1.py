# 정수와 부동 소수점 수 연산
# num_int = 10
# num_float = 3.14
# # Assignment operator: Equal이 아니다!


# # 연산 수행
# result = num_int + num_float # 정수와 부동 소수점 수의 합

# print("결과:", result) # 출력: 결과: 13.14
# print("결과의 자료형:", type(result)) # 출력: 결과의 자료형: <class 'float'>

#____________________________________________________
# 산술 연산자: 수(number)를 계산하는 연산자
# 사칙 연산자 포함: 더하기, 빼기 곱하기, 나누기

# 더하기: 정수 + 정수
# result_1 = 1 + 2
# # 빼기: 정수와 실수의 차
# result_2 = 2 - 1.5
# # 곱하기: 정수의 곱
# result_3 = 3 * 2
# # 나누기: 정수의 나눗셈 결과는 실수
# result_4 = 4 / 2

# # 출력 값: 3       0.5        6         2.0
# print(result_1, result_2, result_3, result_4)

# # 출력 값: <class 'int'> <class 'float'> <class 'int'> <class 'float'>
# print(type(result_1), type(result_2), type(result_3), type(result_4))

# 고찰!! 연산 후 출력 데이터 타입:
# 첫 번째와 세 번째 결과는 정수형
# 두 번째와 네 번째 결과는 실수형
#_________________________________________
# 몫(//), 나머지(%) 연산자
# //: 나누기 연산 후 몫 값만 변환

# result_1 = 3 // 2
# result_2 = 3 / 2

# # 출력 값: 1       1.5
# print(result_1, result_2)

# # %: 나누기 연산 후 나머지 값 반환 -> Modulor 연산자
# # 출력 값: 0  1  2  0  1  2
# for divisor in range(6):
#     print(divisor%3)

# # 나머지 연산은 특정 패턴을 찾기위해 빈번하게 사용
# # 예) 특정 반복문 내에서 3번째 반복마다 특정 명령어 실행
# count = 1

# for dan in range(2, 10):
#     for num in range(1, 10):
#         print(dan, "x", num, "=", (dan*num))

#     if count % 3 == 0:
#         print("===========================")

#     count += 1

#___________________________________________________
# # 지수 연산자: **

# # 2의 3승
# result_1 = 2**3

# # 결과 값: 8
# print(result_1)

# # 결과 값: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
# for value in range(11):
#     print(2**value)