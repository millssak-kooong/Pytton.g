# 키보드를 통해 두 개의 실수를 입력받으세요. 이후 사용할 연산자를 선택하고, 최종적으로 결과를 원하는 자료형으로 출력하는 프로그램을 작성한다.

# 1. Before calculate, make a function to decide input value data types.

def changer(a):
    if '.' in a:
        return float(a)
    else:
        return int(a)

# 2. User input two number strings and declare variables.

num1_str = input("첫 번째 값을 입력하세요") # Input the first number.
num1 = changer(num1_str) # Pass that function.

num2_str = input("두 번째 값을 입력하세요") # Input the second number.
num2 = changer(num2_str) # Pass that function.

# 3. User choose an operator.

my_operator = input("연산자를 선택하세요 (+, -, *, / 중 하나 입력)") # Variable declaration

# 4. User choose a type.

my_data_type = input("결과 값 자료형(integer, float, string 중 하나 입력)")

# 5. Make calculation codes with input values.
## Declare a valiable 'calculation'.

if my_operator == "+":
    calculation = num1 + num2
elif my_operator == "-":
    calculation = num1 - num2
elif my_operator == "*":
    calculation = num1 * num2
else:
    calculation = num1 / num2

# 6. Make data type codes with calculation.
## Declare a valiable 'result'.

if my_data_type == "integer":
    result = int(calculation)
if my_data_type == "float":
    result = float(calculation)
if my_data_type == "string":
    result = str(calculation)

# 7. Declare a variable for the result, print the result.

my_result = result

print("결과 값은 아래와 같습니다.")
print(f"{num1} {my_operator} {num2} = {my_result}")