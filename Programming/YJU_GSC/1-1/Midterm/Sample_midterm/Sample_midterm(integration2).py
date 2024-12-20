# 키보드로부터 정수를 입력 받아 다음과 같이 처리하는 프로그램을 작성
## 입력 받은 수가 양수인 경우 "양수"라는 문자열을 출력
## 입력 받은 수가 음수인 경우 "음수"라는 문자열을 출력
## 입력 받은 수가 0인 경우 프로그램 종료

# 1. while문을 사용하여 코드를 작성

while True: # 참인 동안 무한 루프
    num = int(input("정수를 입력하세요")) # 변수를 while 밖에 작성 시 한 번 들어온 값이 걸리는 곳 없이 계속 돌기 때문에, 안에 작성하여 매 값을 입력할 때마다 걸리게 하여 무한루프를 막음
    if num > 0:
        print("양수 입니다.")
    elif num == 0:
        break # 거짓일 때 무한 반복되는 루프를 첫 반복문으로 올라가 깨부순다.
    else:
        print("음수 입니다")

# if 문이기 때문에 false 코드를 순서 상관없이 작성해도 됨.