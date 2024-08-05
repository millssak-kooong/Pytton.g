# 덧셈, 뺄셈, 곱셈, 나눗셈 계산기
## 사용자로부터 2개의 정수 숫자를 받고 그 합, 차 , 곱, 나눗셈의 결과를 출력하는 프로그램


# 1. 사용자에게 2 개의 정수를 받는다.

num1 = int(input("첫 번째 숫자를 입력하세요.: ")) # 첫 번째 정수를 입력한다.
num2 = int(input("두 번째 숫자를 입력하세요.: ")) # 두 번째 정수를 입력한다.

# 2. 입력받은 정수들의 합, 차, 곱, 나눗셈 결과를 계산한다.

add = num1 + num2 # 덧셉은 add
sub = num1 - num2 # 뺄셈은 sub
mul = num1 * num2 # 곱셈은 mul
div = num1 / num2 # 나눈셈은 div

# 3. 계산된 결과를 출력한다. 단, 결과값의 자료형은 float형으로 출력한다.

print("합", float(add))
print("차", float(sub))
print("곱", float(mul))
print("나눗셈", float(div))




###########################################################################################




# # <두 번째 정수가 0일 때 오류 해결 프로그램>
# # 사용자로부터 2개의 정수 숫자를 받고 그 합, 차 , 곱, 나눗셈의 결과를 출력하는 프로그램


# # 1. 사용자에게 2 개의 정수를 받는다.
# # 1-1 첫 번째 정수를 먼저 받는다.

# num1 = int(input("Type the first integer.: "))

# # 1.2 두 번째 정수가 0일 때 오류 메세지와 두 번째 정수를 0이 아닌 정수를 받을 때까지 다시 입력하도록 한다.

# while True:
#     num2 = int(input("Type the second integer.: "))
#     if num2 == 0:
#         print("0 can't divide any number. Retype please.")

#     # 1-3 두 번째 정수가 0이 아니라면 그대로 입력시킨다.
    
#     else:
#         break

# # 2. 입력받은 숫자들의 합, 차, 곱, 나눗셈 결과를 계산한다.

# add = num1 + num2 # 덧셉은 add
# sub = num1 - num2 # 뺄셈은 sub
# mul = num1 * num2 # 곱셈은 mul
# div = num1 / num2 # 나눈셈은 div

# # 3. 계산된 결과를 출력한다.
    
# print("Addition is", float(add))
# print("Subtraction is", float(sub))
# print("Multiplication is", float(mul))
# print("Division is", float(div))