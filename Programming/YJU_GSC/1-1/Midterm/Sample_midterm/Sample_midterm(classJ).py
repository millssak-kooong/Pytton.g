# 사용자로부터 정수를 입력 받아, 두 개의 선택지 중 하나를 선택 받은 후 판독해 주는 프로그램을 작성한다.
## 1. 그 수가 홀수인지 짝수인지 판별
## 2. 그 수가 3의 배수인지 확인
### 그 외의 숫자 입력 시 에러 메세지를 출력

# 1. Make a menu.

print("--------------------------\n1. 홀수 짝수 구분 프로그램\n2. 3의 배수 확인 프로그램\n--------------------------")

# 2. Write a code to get a select of menu.
## Declare a variable with getting a input value.
my_menu = int(input("메뉴를 선택해 주십시오."))

# 3. Write a code when you would get selection '1'.
if my_menu == 1:
    input_integer1 = int(input("홀수 짝수 구분 프로그램을 선택하셨습니다.\n정수 값을 입력하세요."))
    if input_integer1 % 2 == 0:
        print(f"입력하신 값 {input_integer1} 짝수입니다.")
    else:
        print(f"입력하신 값 {input_integer1} 홀수입니다.")

# 4. Write a code when you would get selection '2'.
elif my_menu == 2:
    input_integer2 = int(input("3의 배수 확인 프로그램을 선택하셨습니다.\n정수 값을 입력하세요."))
    if input_integer2 % 3 == 0:
        print(f"입력하신 값 {input_integer2}, 3의 배수입니다.")
    else:
        print(f"입력하신 값 {input_integer2}, 3의 배수가 아닙니다.")

# 5. Write a code when you would get other than selection '1' or '2'.
else:
    print(f"입력하신 값 {my_menu}은 유효하지 않은 메뉴 선택 값입니다. 메뉴 선택은 1과 2만 가능합니다.")