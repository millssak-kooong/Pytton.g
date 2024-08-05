
import random


def print_menu():
    width = 15
    print("-" * width)
    print("1. 구구단 출력")
    print("2. 삼각형 출력")
    print("3. 종료")
    print("-" * width)
    
def is_valid_num(arg_start, arg_end, *args):
    
    for value in args:
        if not (arg_start <= value <= arg_end):
            return False
            
    return True

def print_mul_table():
    
    while True:
        input_value = input("출력할 단을 입력하세요: ")
        
        input_list = input_value.split("~")
        input_list = [int(value) for value in input_list]
            
        if is_valid_num(2, 9, *input_list):
            break
            
        print("2~9 정수를 입력 하세요")
              
    
    # 구구단을 출력
    start = input_list[0]
    end = input_list[1] if len(input_list) > 1 else input_list[0]
    
    for dan in range(start, end + 1):
        for num in range(1, 10):
            print(f"{dan} X {num} = {dan * num}")
        print()
        
def print_triangle():
    
    while True:
        row_num = int(input("삼각형의 높이를 입력하세요: "))
        
        if is_valid_num(2, 3, row_num):
            break
        
        print("2~3 값을 입력 하세요")
    
    # rand_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rand_list = [value for value in range(10)]
    
    for rnum in range(row_num):
        # 공백 출력
        print(" " * (row_num - rnum - 1), end="")
         
        # 난수 값 출력
        for _ in range(rnum + 1):
            rand_num = rand_list[random.randint(0, len(rand_list) - 1)]
            rand_list.remove(rand_num)
            
            print(rand_num, end="")
            
        # 개행 문자
        print()
    
    
while True:

    # 메뉴 출력
    print_menu()

    input_value = int(input("메뉴를 선택 해주세요: "))

    if not (1 <= input_value <= 3):
        print("1~3 정수를 입력하세요")
        continue
    
    # 1. 구구단 실행
    if input_value == 1:
        print_mul_table()
    # 2. 삼각형 출력
    elif input_value == 2:
        print_triangle()
    # 3. 종료
    elif input_value == 3:
        print("종료")
        break