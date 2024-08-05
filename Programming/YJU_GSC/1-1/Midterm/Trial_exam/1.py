# 교수님 풀이

while True:
    # 메뉴 출력
    print("-" * 10)
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("-" * 10)

    # 메뉴 값 입력
    selected_menu = input("메뉴 값을 입력하세요! : ")
    
    # 메뉴 값 == 1
    if selected_menu == '1':
        while True:
            # 구구단의 단 입력
            dan = int(input("단을 입력 하세요: "))
            
            if 2 <= dan <= 9:
                # 해당 단의 구구단 출력
                for num in range(1, 10):
                    print(dan, " X ", num, " = ", dan * num)
                    
                break
                    
            print("단은 2~9사이의 정수 값 입력")
            
    # 메뉴 값 == 2
    elif selected_menu == '2':
        # 프로그램 종료
        print("프로그램 종료")
        break
    # 메뉴 값이 != 1 and 메뉴 값 != 2
    # 에러메시지지 출력
    else:
        print("메뉴 값은 1 또는 2만 입력 ")