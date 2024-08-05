# 산술 연산자
# +, -, *, /

# 묵시적 형변환
print(type(2 + 3.0)) # implicit type conversion!!: 2 + 3.0 -> float(2) + 3.0

# 2     + 3.0
# int   + float -> float
# float ? (int -> float) 형변환(Type conversion)을 한다.

input_str = input("정수를 입력하세요")

                           # 명시적 형변환
input_int = int(input_str) # explicit type conversion!!
# input_str: str -> integer by using int() function

#__________________________________________________________________

for value in range(1, 11):
    print(str(value) + "번째 값")

##################################

bar = (2.0 + 3) * 40

# 1) 2.0 + 3 -> 2.0 + float(3)
# 2) 5.0 * 4
# 3) 5.0 * float(4)
# 4) 20.0