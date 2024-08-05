import random


while True:
    # 1. Show menu
    print("-------------------\n1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료\n-------------------")
    menu = int(input("원하는 메뉴 번호를 입력하세요: "))
    
    # 2. Multipliction table
    if menu == 1:
        while True: # 구구단을 원하는 단만 출력, 잘못 입력하면 재입력 요구
            dan = []
            dan += input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n")
            pass # print(dan) 인덱스 확인용
            
            if len(dan) == 1: # 한 단만 입력했을 때
                if 2 <= int(dan[0]) <= 9:
                    for row in dan[0]:
                        for column in range(1, 10):
                            print(f"{row} X {column} = {int(row) * column}")
                    break
                else:
                    print("재입력")
                
            else: # 여러 단 출력 할 때
                if 2 <= int(dan[0]) <= 9: # 일단 첫 번 째 인덱스 값부터 안전하게 확인해 나간다
                    if dan[1] == "~":
                        if 2 <= int(dan[2]) <= 9:
                            for row in range(int(dan[0]), int(dan[2]) + 1):
                                for column in range(1, 10):
                                    print(f"{row} X {column} = {row * column}")
                                print("----------")
                            break
                        else:
                            print("재입력")
                    else:
                        print("재입력")
                else:
                    print("재입력")

    # 3. Triangle
    elif menu == 2:
        while True:
            height = int(input("삼각형의 높이 줄 수를 입력하세요(2 이상 3 이하)\n"))
            
            if 2 <= height <= 3:
                # 중복 되지 않는 난 수 3개 또는 6개 받기
                while True:
                    xbox = []
                    for _ in range(6):
                        xbox.append(random.randint(0, 9))
                    if xbox[0] not in xbox[1:6:1]:
                        if xbox[1] not in xbox[2:6:1]:
                            if xbox[2] not in xbox[3:6:1]:
                                if xbox[3] not in xbox[4:6:1]:
                                    if xbox[4] not in xbox[5:6:1]:
                                        break
                # print(xbox) 확인용

                # 생성된 난수 6개로 삼각형 만들기
                #--- 삼각형도 6난수 랜덤으로 만들기 ---#
                # a = random.randint(0,5)
                # print(xbox[a])

                if height == 2:
                    print(f" {xbox[0]}\n{xbox[1]}{xbox[2]}")
                else:
                    print(f"  {xbox[0]}\n {xbox[1]}{xbox[2]}\n{xbox[3]}{xbox[4]}{xbox[5]}")
                break
        
        
            # 예외 처리
            else: 
                print("2 또는 3을 입력하세요.")

    # 4. Off
    elif menu == 3:
        print("프로그램을 종료합니다.")
        break

    else:
        print("1~3 사이의 값을 입력하세요")