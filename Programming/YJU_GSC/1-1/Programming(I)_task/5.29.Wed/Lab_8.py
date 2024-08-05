# while 문과 break 문을 사용하여 1부터 100 사이의 숫자를 맞추는 게임
# 사용자가 숫자를 맞출 때까지 반복하고, 맞추면 반복을 종료
# 정답 숫자는 랜덤 함수를 이용하여 1에서 100사이 임의 정수 선택
################################################################
# 1
import random

x = random.randint(1, 101)

while True:
    y = int(input("1~100 사이의 랜덤 숫자를 맞추시오: "))
    if x == y:
        print("정답입니다!")
        break
    elif x < y:
        print("더 작은 숫자입니다.")
    else:
        print("더 큰 숫자입니다.")

#________________________________________
# 2

import random

x = random.randint(1, 101)

while True:
    y = int(input("1~100 사이의 랜덤 숫자를 맞추시오: "))
    msg = ""
    
    if x < y:
        msg = "더 작은 숫자입니다."
    elif x > y:
        msg = "더 큰 숫자입니다."
    else:
        msg = "정답입니다!"
        print(msg)
        break