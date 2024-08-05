# 형변환 (Type conversion): 변수나 상수의 자료형을 변환하는 것

bar = 2
foo = 3.0

print(type(str(bar))), type(int(foo))
# <class 'str'> <class 'int'>

print(type(float(2))), type(int(2, 0))
# <class 'float'> <class 'int'>

#___________________________________________

input_int = int(input("첫 번째 입력 값: "))
input_float = float(input("두 번째 입력 값: "))

sum = input_int + input_float

#___________________________________________

sum = 1 + "1"
# int + str
# erro
print(sum) # erro

#___________________________________________

sum = 1 + True
# 1 + True
# int + boolean
# int + int(True)
# 1 + 1
# 2
print(sum) # 2

#___________________________________________

sum = 3.0 + True + 2
# 3.0 + True + 2
# float + boolean + int
# float + boolean
# 3.0 + float(True)
# 3.0 + 1.0 -> 4.0
# 4.0 + 2
# float + int
# 4.0 + float(2)
# 4.0 + 2.0
# 6.0
print(sum) # 6.0