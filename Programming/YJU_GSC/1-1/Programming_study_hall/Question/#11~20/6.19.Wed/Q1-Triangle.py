# 2024.6.25.화 #
################
# 1. Show menu
print("-------------------\n1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료\n-------------------")
#----------------------------------------------
import random
# 1. 줄 수를 입력 받고 예외도 작성한다.
# 2. 0~9 사이의 중복되지 않는 난수를 입력 받은 줄 수에 맞게 출력한다.
# 3. 줄 수만큼 개행문자를 사용해서 모양 만들기

menu = int(input("원하는 메뉴 번호를 입력하세요: "))
if menu == 2:
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



# no중복 난수 만들기
### if xbox[1] not in xbox[0:0:1]:
###     print(xbox[0:2:1])

# while True:
#     xbox = [] # list가 while문 밖에 있으면 무한 루프에 빠진다.
#     for _ in range(6): # 한 번에 6개 받아 놓고 시작
#         xbox.append(random.randint(0, 9)) # xbox += (str으로 바꿔 줘야 리스트에 문자로 들어 가 진다).random.randint(0, 9)
#     if xbox[0] not in xbox[1:6:1]:
#         if xbox[1] not in xbox[2:6:1]:
#             if xbox[2] not in xbox[3:6:1]:
#                 if xbox[3] not in xbox[4:6:1]:
#                     if xbox[4] not in xbox[5:6:1]:
#                         print(xbox)
#                         break