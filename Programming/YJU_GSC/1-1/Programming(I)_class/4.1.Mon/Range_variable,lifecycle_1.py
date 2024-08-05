#                   Check point 1                Check point 1
# 접근 범위      변수 사용이 가능한 지점       변수 사용이 종료된는 지점
# 생명 주기              출생                        소멸(죽음)


bar = 2 # bar라는 변수가 2라는 초기값을 가지면서, 메모리 내 생성된다. 변수가 출생.
# bar라는 변수가 사용 가능 한 시작 줄(6번), 변수에 접근 가능한 범위


print(bar) # bar 변수의 값을 GET해서 print() 함수를 이용해 화면에 출력
# 위 10번 줄 이 프로그램의 끝나는 마지막 줄, bar라는 변수가 소멸(죽는)되는 지점

#____________________________________________________________________________

# 구조적 언어(에서 핵심 2가지 변수와 함수)
# 1. 전역 변수(Global variable)
# 2. 지역 변수(Local variable)

#____________________________________________________________________________

# 함수 Function이 왜 필요할까요?
def printSum(argA, argB, argC):                  # 함수 정의
    sum = argA + argB + argC
    print(sum)


input1 = int(input("값을 입력하세요"))
input2 = int(input("값을 입력하세요"))
input3 = int(input("값을 입력하세요"))

printSum(input1, input2, input3)                 # 함수 호출

input1 = int(input("값을 입력하세요"))
input2 = int(input("값을 입력하세요"))
input3 = int(input("값을 입력하세요"))

printSum(input1, input2, input3)                 # 함수 호출

input1 = int(input("값을 입력하세요"))
input2 = int(input("값을 입력하세요"))
input3 = int(input("값을 입력하세요"))

printSum(input1, input2, input3)                 # 함수 호출

input1 = int(input("값을 입력하세요"))
input2 = int(input("값을 입력하세요"))
input3 = int(input("값을 입력하세요"))

printSum(input1, input2, input3)                 # 함수 호출

#     .................... 계속 '반복'