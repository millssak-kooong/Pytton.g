# 1. Show menu
print("-------------------\n1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료\n-------------------")

#2. Let user select a menu
menu = int(input("원하는 메뉴 번호를 입력하세요: "))

# 3. Menu 1
if menu == 1:
    while True:
        select = input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n")
        box = []
        box += select
    # print(box)
#------------------------------------
    
        if len(select) == 1: # A dan
            if int(box[0]) < 2: # 어짜피 범위 밖의 정수는 앞자리가 무조건 1이 오니까. (20 이상 수는 일단 배제)
                print("재입력 하시오. 정수의 범위는 2~9. (예: 2, 2~5)\n")
            else:
                for row in range(int(select), int(select) + 1):
                    for column in range(1, 10):
                        print(f"{row} X {column} = {row * column}")
                    print("----------")
                break
        else: # Dans
            if int(box[0]) < 2 or int(box[2]) < 2: # 어짜피 범위 밖의 정수는 앞자리가 무조건 1이 오니까. (20 이상 수는 일단 배제)
                print("재입력 하시오. 정수의 범위는 2~9. (예: 2, 2~5)\n")
            elif int(box[0]) == int(box[2]):
                print("재입력 하시오. 정수의 범위는 2~9. (예: 2, 2~5)\n")
            else:
                del box[1]
                for row in range(int(box[0]), int(box[1]) + 1):
                    for column in range(1, 10):
                        print(f"{row} X {column} = {row * column}")
                    print("----------")
                break

###################################
# 원하는 단 출력 코드

    # if "~" in select: # More than 2 dans
    #     del box[1]
    #     for row in range(int(box[0]), int(box[1]) + 1):
    #         for column in range(1, 10):
    #             print(f"{row} X {column} = {row * column}")
    #         print("----------")
    # else: # One dan
    #     for row in range(int(select), int(select) + 1):
    #         for column in range(1, 10):
    #             print(f"{row} X {column} = {row * column}")
    #         print("----------")



# 예외 처리 코드 Out of range dan
    # if len(select) == 1:
    #     if int(box[0]) < 2:
    #         print("재입력 하시오. 정수의 범위는 2~9. (예: 2, 2~5)\n")
    #     else:
    #         print("ok")
    # else: # More than one dan
    #     if box[1] != "~":
    #         print("재입력 하시오. 정수의 범위는 2~9. (예: 2, 2~5)\n")

    #         if int(box[0]) < 2 or int(box[2]) < 2:
    #             print("재입력 하시오. 정수의 범위는 2~9. (예: 2, 2~5)\n")
    #         elif int(box[0]) == int(box[2]):
    #             print("재입력 하시오. 정수의 범위는 2~9. (예: 2, 2~5)\n")
    #     else:
    #         print("ok")

    
############################################################################
############################################################################
### 손도 못 댈 때 교수님 조언 ###

# 예외처리는 마지막에 구현

# 메뉴 출력
# print("-" * 20)
# print("1. 구구단 출력")
# print("2. 삼각형 출력")
# print("3. 종료")

# # 사용자로부터 값 입력
# input_value = int(input("값을 입력하세요: "))

# # 해당 메뉴 실행
# if input_value == 1:
#     print("구구단 실행")
# elif input_value == 2:
#     print("삼각형 실행")                
# elif input_value == 3:
#     print("프로그램 종료")
# else:
#     print("1~3 사이 정수를 입력하세요")