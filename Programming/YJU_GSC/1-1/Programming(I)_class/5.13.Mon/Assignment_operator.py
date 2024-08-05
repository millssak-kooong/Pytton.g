# Multiple assignment : 다중 대입

bar, foo, kin = 10, 20, 30

print(f"{bar}, {foo}, {kin}")

#_________________________________

def getValue():
    return 2, 3, 4, 5

print(getValue())

print(type(getValue())) # tuple

#_________________________________

bar = [2, 3, 4, 5]
foo = (6, 7, 8, 9) # ( ) <- tuple
kin = 20, 30, 40, 60 # ( ) x <- tuple

print(bar[0])
print(foo[0])
print(kin)

bar[0] = 20
foo[0] = 60

#_________________________________

# Collection unpacking

bar = [9, 4, 5, 7] # 9, 4, 5, 7 -> List로 packing

seo, foo, pos, kin = bar # 좌항에 ','가 와야 unpacking 된다.

print(f"{seo}, {foo}, {pos}, {kin}")

#___________________________________

def getValue():
    return 2, 3, 4, 5

# Collection Unpacnkig

bar, foo, pos, kin = getValue()

#__________________________________

# Walrus operator
# Python 3.8부터 나옴, 교수님은 추천하지 않음
# version이 달라 호환되지 않을 수 있음
# 최신 version이 다 좋은 건 아님

bar = "hello"

for char in bar:
    print(char, end = "")

print()

for char in (foo := "world"): # 변수에 값을 대입과 동시에 대입된 값을 바로 평가(evaluation)한다, 코드의 간결성
    print(char, end = "")

#_______________________________________

def getCalcValues(argA, argB):
    # argA와 argB의 +, -, *, / 값을 반환하는 함수 작성
    # 값 반환 시 tuple 자료형으로...
    return argA + argB, argA - argB, argA * argB, argA / argB

sum, subtract, multiply, division = getCalcValues(2, 3)

print(f"{sum}, {subtract}, {multiply}, {division}")

kin = getCalcValues(2, 3)

foo = list(kin)
foo[0] = foo[0] + 1
print(foo[0])

#_______________________________________

bar = 0

bar = bar + 1

bar += 1
bar -= 1
bar *= 1
bar /= 1
bar //= 1
bar %= 1

#________________________________________

# Membership operator
# in, not in
# A in B
# A 값, B sequential object
# 결과 값은 Boolean

# in 일 때 함수
def myInOperator(argValue, argSeqObj):
    for value in argSeqObj:
        if value == argValue:
            return True
        
    return False

# not in 일 때 함수
## value가 argValue 안에 없니?
def myInOperator(argValue, argSeqObj):
    for value in argSeqObj:
        if value == argValue:
            return False # 아니(False) 있어
        
    return True # 응(True) 없어

print(myInOperator(3, [2, 3, 4]))

#____________________________________
# a가 abc 안에 있으면 참 없으면 거짓

print("a" in "abc")

#_________________________________
# bar 안에 4가 있느냐 없느냐

bar = [3, 4, 5, 6]

print(4 in bar)
print(4 not in bar)


#_________________________________________

# Identity Operator
# is, is not

bar = [2, 3, 4]
foo = [2, 3, 4]
pos = bar

if bar == foo:
    print("참")
else:
    print("거짓")

if bar is foo:
    print("참")
else:
    print("거짓")

if bar is pos:
    print("참")
else:
    print("거짓")