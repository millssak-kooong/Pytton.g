# def 함수 이름(매개변수):
#    함수 호출 시 실행 코드


# 함수 호출 시 입력 값을 전달 할 수 있다.
# -> 1) Argument(인자 값)
# -> 2) Parameter(매개변수)
# def 함수 이름(매개변수):
#    함수 호출 시 실행 코드


# 함수 호출 시 입력 값을 전달 할 수 있다.
# -> 1) Argument(인자 값)
# -> 2) Parameter(매개변수)

def print_name(arg_name, arg_msg): # arg_name -> 매개변수 Parameter
    print(arg_name, arg_msg)

print_name("Richard", "안녕") # "Richard" -> 인자 값(Argument)

#-------------------------------

def get_sum_avg (arg_a, arg_b, arg_c):
    sum = arg_a, arg_b, arg_c
    avg = sum / 3
    return sum, avg # -> (sum, avg)
# 함수 반환 값이 두 개 이상이면 -> 자동으로 tuple 자료형으로 구성 후 반환
sum, avg = get_sum_avg(1, 2, 3)

#######################################

# Call-by-primitive: sol, msg
# Call-by-reference: bar, foo, kin

sol = 4 # Number -> Primitive

bar = [3, 4] # 참조 변수로서 원소의 주소값만 갖고 있다.

foo = [5, 6]

kin = bar # 참조 변수로서 원소의 주소값만 갖고 있다.

kin[0] = 1 # 'kin[0]' = 수식 expression, '[]' = 연산자 operator

print(bar, foo, kin) # [1, 4] [5, 6] [1, 4]

msg = "hello"

kin.append(20)

foo, kin = 7, 8 # foo의 [5, 6]은 좀비 메모리가 된다. Garbage Collector(GC)에게 먹힌다.

[5, 3, 1]