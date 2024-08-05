# def 함수명(인자값 Argument(정확히는'매개변수 Parametor'=변수니까 입력값을 저장)):
#     함수 호출 시 실행 명령어

# 함수 정의: -> 1번
# 정의된 함수는 인터프리터에게 알려준다.
def print_name(name):
    print(name, "님 안녕하세요")

# 함수 호출: -> 2번
print_name("리차드")
print_name("정영철")

##############################################
# 함수 사용의 순서
# 1) 함수를 정의한다
# 2) 정의된 함수를 호출한다.


# 정수 3개를 입력 받아 합계와 평균을 출력하는 프로그램을 작성하라.

def get_int(arg_num):
    input_values = []
    for _ in range(arg_num):
        input_values.append(int(input("입력값: ")))
        
    return input_values

def get_sum_avg(arg_list):
    sum = 0
    for value in arg_list:
        sum += value
    
    avg = sum / len(arg_list)
    
    return sum, avg

def get_sum(arg_list):
    sum = 0
    for value in arg_list:
        sum += value
    
    return sum
 

input_list = get_int(13)

sum, avg = get_sum_avg(input_list)

print(sum, avg)

#-----------------------------------
# 내가 짠 거
def calculation():
    sum = 0
    for x in range(3):
        x = int(input("Input an integer: "))
        sum += x
    print(sum, sum / 3)

print(calculation())
#############################################

def get_sum_avg(argA, argB, argC, argd):
    sum = argA + argB + argC + argd
    avg = sum / 4
    return sum, avg # 반환값이 두 개 이상이면 tuple로 변환 후 반환한다. Python에서만 가능.

sum, avg = get_sum_avg(1, 2, 3, 4)
print(sum, avg)
print(type(get_sum_avg(1, 2, 3, 4)))

Value = get_sum_avg(1, 2, 3, 4) # 이건 잘 안 쓰고 위 방법을 대부분 쓴다.
print(Value[0], Value[1])

############################################
# Call-by-primitive
# Call-by-reference

bar = [20, 30, 40]

def foo(argList): # Call-by-reference
    argList[2] = 100
    argList[0] = 300

foo(bar)

print(bar)