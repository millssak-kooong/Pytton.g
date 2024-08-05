# 2024.6.22.토 #
################
# 1. Show menu
print("-------------------\n1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료\n-------------------")
#----------------------------------------------
# 1. 원하는 단을 양식에 맞게 입력 받는다.
# 2. 정확한 단의 입력값을 입력했는지 안 했는지 구분하여 재입력을 요구할지 판단하기 위해 정해지지 않은 반복문 while을 사용.
# 3. 정확한 입력값이라면 한 단인지 여러 단인지 판별
# 4. 한 단일 때 엽력값이 유효한지 판별해서 유효하면 구구단 출력 후 종료, 아니면 재입력 요구.
# 5. 한 단이 아닐 때, 즉 여러 단일 때 인덱스 번호를 이용해 한 자리 한 자리 양식에 맞는 입력 값인지 판별해 나가고 아닐 때 마다 재입력 요구하고 마지막 조건까지 맞다면 구구단 출력 후 종료
# 6. 구구단 작성 후 4, 5 번 구구단 출력 라인에 넣는다.

menu = int(input("원하는 메뉴 번호를 입력하세요: "))

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

# 구구단 만들기
# for row in range(2, 10):
#     for column in range(1, 10):
#         print(f"{row} X {column} = {row * column}")
#     print("----------")