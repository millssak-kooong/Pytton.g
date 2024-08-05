# call-by-reference, call-by-value

bar = 3

def foo(bar): # call-by-value
    bar = bar + 1

foo(bar)

print(bar) # 3

#-------------------------------
# argument
# 1) positional argument
def foo(arg_a, arg_b, arg_c):
    print(arg_a, arg_b, arg_c)
foo(1, 2, 3)

# 2) keyword argument
def pos(arg_a, arg_b, arg_c):
    print(arg_a, arg_b, arg_c)
pos(arg_c = 1, arg_a = 2, arg_b = 3)

# 3) default argument

def kin(arg_a = 1, arg_b = 2, arg_c = 3, arg_d = 4):
    print(arg_a, arg_b, arg_c, arg_d)
kin() # 1 2 3 4
kin(6, 7, 8, 9) # 6 7 8 9
kin(6) # 6 2 3 4
kin(6, 7) # 6 7 3 4
kin(6, 7, arg_d = 10) # 6 7 3 10

print("hello", end = "")

#  a) 모든 파라메터에 초기 값을 설정한다.
#  b) 초기 값을 가지는 파라메터는 제일 뒷쪽에 위치한다.
def pos(arg_a, arg_b, arg_c = 3, arg_d = 4):
    print(arg_a, arg_b, arg_c, arg_d)

# 4. variable parameter: 가변 파라메터
# 1) *
# 2) **
         # * -> 가변: tuple로 받겠다.
def foo(*args):
    print(len(args))
    for value in args:
        print(value)

foo(1) # 1
foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) # 12

#-------------------------------

def bar(*args):
    if len(args) == 1:
        start = end = args[0]
    elif len(args) == 2:
        start, end = args
    else:
        return
    
    for dan in range(start, end + 1):
        for num in range(1, 10):
            print(f"{dan} X {num} = {dan * num}")
bar(2)
bar(2, 3)

#-------------------------------

def foo(**args):
    print(len(args))
    
    for key, value in args.items():
        print(f"key: {key}, value:{value}")
foo(test = 2, king = 3) # 1
foo(test = 2, king = 3, lion = 4) # 1

#--------------------------------

def foo(arg_a, arg_b, arg_c, arg_d, arg_e):
    print(arg_a, arg_b, arg_c, arg_d, arg_e)

# foo(1, 2, 3, 4, 5)

# arg_list = [value for valuein range(1, 6)]
arg_list = [1, 2, 3, 4, 5]

foo(*arg_list)

#-------------------------------
# 구구단으로 프로그램 출력

def printMulTable(arg_start, arg_end = None):
    # 인자 값이 한 개가 입력되었을 경우
    # arg_start 값만 출력한다.
    # range(arg_start, arg_start + 1)
    if arg_end == None:
        arg_end = arg_start

    for dan in range(arg_start, arg_end):
        for num in range(1, 10):
            print(f"{dan} X {num} = {dan * num}")

printMulTable(2, 5)
printMulTable(2)