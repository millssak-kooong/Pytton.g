print(type(1 == 1), type(1 != 1))
print(type(1 > 1), type(1 >= 1))
print(type(1 < 2), type(1 <= 2))

#_____________________________________

value = int(input("정수 입력"))

if value > 3: # 6 종류 비교 연산자 모두 비교해 보기
    print("참")
else:
    print("거짓")

#_______________________________________________________
# 비교 값이 실수면? 단, 입력 값은 정수
# 입력 값도 묵시적 형변환을 하여 실수로 비교를 한다.

value = int(input("정수 입력"))

if value > 3.0: # 6 종류 비교 연산자 모두 비교해 보기
    print("참")
else:
    print("거짓")

#_______________________________________________________

c = 2
# Chained comparison(Python의 철학: 쉽게!)
# 1 < c <= 3 -> C > 1 and c <=3 : 컴퓨터는 모두 끊어서 이해한다.

if 1 < c <= 3:
    print("참")
else:
    print("거짓")

#_______________________________________________________________

print(2 > 3 < 4)
print(2 < 4 < 3 < 6 < 8)
# 왼쪽 -> 오른쪽
# 1. 2 > 3 -> False -> 종료
# 2-1. 2 < 4 -> True
# 2-2. 4 < 3 -> False