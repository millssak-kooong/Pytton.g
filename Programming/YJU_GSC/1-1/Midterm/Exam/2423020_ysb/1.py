# 2024.04.24.수
# 10:40 ~ 11:40
# 중간 고사 문제 1
# 2423020_윤성빈
#_________________________________________________________________________________________

# 키보드로부터 정수 5개를 입력받아 합계와 평균을 출력하는 프로그램

# 1. 사용자로부터 정수 5개를 입력 받기
## int를 사용하여 string이 아닌 integer로 자료형 변환

num1 = int(input("1번째 값을 입력하세요: ")) # 첫 번째 정수 값 받으면서 변수 선언
num2 = int(input("2번째 값을 입력하세요: ")) # 두 번째 정수 값 받으면서 변수 선언
num3 = int(input("3번째 값을 입력하세요: ")) # 세 번째 정수 값 받으면서 변수 선언
num4 = int(input("4번째 값을 입력하세요: ")) # 네 번째 정수 값 받으면서 변수 선언
num5 = int(input("5번째 값을 입력하세요: ")) # 다섯 번째 정수 값 받으면서 변수 선언

# 2. 입력 값 합계 계산

sum = num1 + num2 + num3 + num4 + num5 # '+' 연산자를 사용하여 합계 계산 변수 선언

# 3. 입력 값 평균 계산
## 20번 라인에서 선언된 sum 변수를 이용

avg = sum / 5 # '/' 연산자를 사용하여 평균 계산 변수 선언

# 4. 결과 출력
## 20, 25 라인에서 선언된 변수 sum과 avg를 사용

print("합계:", sum) # 합계 출력
print("평균:", float(avg)) # 평균(자료형은 실수) 출력