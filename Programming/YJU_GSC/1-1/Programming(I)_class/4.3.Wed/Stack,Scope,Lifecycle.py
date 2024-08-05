def bar():
    msg = "안녕하세요"
    foo() # 2
    return msg # 9

def foo():
    print("foo")# 3
    pos() # 4
    print("1") # 6
    kin() # 7

def pos():
    print("pos") # 5

def kin():
    print("kin") # 8

bar() # 1(Start), # 10(End)

#_____________________________________________________

def foo():
    msg = "hello" # 23에서 탄생, 24를 지나면 죽음(호출된 함수가 종료될 때) # 접근 범위 Scope: 24 ~ 25
    print(msg)

msg = "안녕하세요" # 26에서 탄생, 29에서 죽음 # 접근 범위 Scope: 27 ~ 29

print(msg)

#_____________________________________________________

def foo():
    msg = "hello"
    print(greeting)

greeting = "안녕하세요"

print(msg)

#_____________________________________________________
# 변수를 GET 할 경우 Scope chainning
# 1) 전역코드 -> 지역 변수: 원천적 접근 불가
# 2) 지역코드 -> 전역 변수: 접근 가능, Scope chainning 규칙에 의거
# Local -> Enclosed -> Global -> Built-in (LEGB)

# 변수를 SET 할 경우 Scope chainning => 원천적으로 불가.

def foo():
    global msg

    msg = "hello" # 전역 변수에 지역 변수 msg를 SET 하고 싶을 때, global 명령어를 사용
    
msg = ""

foo()

print(msg)