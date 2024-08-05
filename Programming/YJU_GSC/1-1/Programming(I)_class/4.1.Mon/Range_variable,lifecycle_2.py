def getAvg(a, b, c): # a, b, c는 매개 변수 (Parameter Variable)
                     # 이 함수의 매개 변수는 3개
                     # 매개 변수는 무한대로 만들 수 있는데, 0개일 수도 있다.이럴 땐 인자값을 넣으면 안 되고 그냥 호출만 하는 것이다.)

#________________________________________________
# 함수를 호출하고 매개 변수가 선언이 될 때 매개 변수는 할당된다.

def sayName(argName): # 매개변수
    print("안녕하세요", argName)

sayName("정영철") # 정영철은 '인자값 Argument'


#________________________________________________
# 3개의 수를 입력 받아 평균을 계산해줘

def getAvg(argA, argB, argC):
    sum = argA + argB + argC
    avg = sum / 3
    return avg
# return의 2가지 의미
# 1. 함수를 종료하십시오.
# 2. return 옆에 있는 값을 함수 호출 쪽으로 반환해라.

result = getAvg(1, 2, 3) # getAvg값을 호출하고 1, 2, 3 인자값을 입력한다.
result = getAvg(4, 5, 6)
result = getAvg(7, 8, 9)

#_________________________________________________________________

def getAvg(argA, argB, argC): # return은 여러번 써도 된다.
    if argA < 0 or argB < 0 or argC < 0:
        return "erro"
    
    sum = argA + argB + argC
    avg = sum / 3
    return avg

result = getAvg(1, 2, 3)
result = getAvg(4, -5, 6)
result = getAvg(7, 8, 9)

#__________________________________________________________________
# 왜 hello만 나오는가?
msg = "hello"

def setMsg(argMsg):
    msg = argMsg + "hello"

setMsg("안녕하세요")

print(msg) # "안녕하세요 hello"