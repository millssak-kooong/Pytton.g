# incrementCount 함수 정의:
#  - 전역 변수 count의 값을 1 증가
def incrementCount():
    global count;
    count = count + 1

# decrementCount 함수 정의:
#  - 전역 변수 count의 값을 1 감소
def decrementCount():
    global count;
    count = count - 1

# 전역 변수 count를 1로 초기화
count = 1

incrementCount()
print(count)

decrementCount()
print(count)

incrementCount()
print(count)
incrementCount()
print(count)

#_________________________________________

def bar():
    msg1 = "<< " + name

    msg2 = foo(msg1)
    msg2 += " " # 왜 이 라인이 없으면 띄어쓰기가 안 되는 걸까?

    msg3 = pos(msg2)
    msg3 += " "

    return msg3

def foo(argF):
    msg = argF + "님"
    return msg

def pos(argP):
    msg = argP + "안녕하세요"
    return msg

name = "홍길동"

result = bar()

print(result)