# 정수 입력 받고 정수 만큼 가로 X 세로 바둑판 출력
## * 연산자 사용 금지, 반복문 사용


input_value = int(input("입력 값: "))

for _ in range(0, input_value): # 세로 열 반복
    
    for _ in range(0, input_value): # 가로 열 반복 
        print("*", end = "")
    print() # 들여 쓰기 위치 이해하기


# enter('\n' = 개행 문자 New line character) 키도 하나의 문자다. <-> 공간을 주는 tap '\t'
# 중첩 for 문이 있다면 안에서부터 해석해라

#_____________________________________________________


for _ in range(2):
    for _ in range(4):
       print("*", end="")
    print("\n")

# 같은 코드

for _ in range(2):
    for _ in range(4):
       print("*", end="")
    print("")
    print("")