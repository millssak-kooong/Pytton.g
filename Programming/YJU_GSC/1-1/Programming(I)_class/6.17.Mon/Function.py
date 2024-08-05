# Overloading
# 함수와 메서드에 적용이 된다.
# 사용 목적은? 프로그래머에게 코드 작성의 편리성을 제공하기 위해.
# 파이썬에서는 지원되지 않는다.
# 가변 위치 인자를 이용하면 함수 오버로딩 기능을 구현 할 수 있다.

# 실해 안 됨
def bar(a, b):
    return a + b

def bar(a, b, c):
    return a + b + c

def bar(a, b, c, d):
    return a + b + c + d

print(bar(2, 3))
print(bar(2, 3, 4))
print(bar(2, 3, 4, 5))

# 실행 됨
def bar(*args):
    return sum(args)

print(bar(2, 3))
print(bar(2, 3, 4))
print(bar(2, 3, 4, 5))

#------------------------
def bar(arg_fnc):
    arg_fnc()

def foo():
    print("안녕하세요: ")

bar(foo)
# 출력: 안녕하세요: 
#-------------------------------------------
# 주민등록 검사 프로그램
# 790608-2552416 = Valid
# 040425-2454578 = Invalid

def get_check_digit(arg_ssid):
    #weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    weight = [(value % 8) + 2 for value in range(12)]
    
    ssid = [int(value) for value in arg_ssid]
    
    sum_values = sum([ssid[index] * weight[index] for index in range(12)])
    
    return (11 - sum_values % 11) % 10
    

# 유효한 주민번호 -> True else False
def is_valid_ssid(arg_ssid):
    
    arg_ssid = arg_ssid.replace("-", "")
    
    if len(arg_ssid) != 13:
        return False
    
    # 체크값 계산 알고리즘 구현 필요
    check_digit = get_check_digit(arg_ssid[:-1]) 
    
    if check_digit == int(arg_ssid[-1]):
        return True
    else:
        return False



print(is_valid_ssid("790608-2552416"))
print(is_valid_ssid("040425-2454578"))