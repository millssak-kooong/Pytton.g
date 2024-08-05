import random

# 가위, 바위, 보 게임 만들기
# count_win = 0
# count_lose = 0
# count_draw = 0

count_win, count_lose, count_draw = 0, 0, 0

while True:
    # 승리 회수가 2번 이상 또는 패배 회수가 2번 이상이면, 프로그램 종료
    if count_win >= 2 or count_lose >= 2:
        print("승리 : ", "사용자" if count_win >= 2 else "컴퓨터")
        print(f"전적 : {count_win}승 {count_lose}패 {count_draw}무")
        
        # if count_win >= 2:
        #     print("사용자")
        # else:
        #     print("컴퓨터")
            
        break
    
    
    while True:
        # 사용자로부터 입력 받기
        input_user = input("가위 바위 보 중 입력: ")
        
        if input_user == "가위" or input_user == "바위" or input_user == "보":
            break
        
        print("가위 바위 보 중에서 하나를 입력하세요")


    # 컴퓨터가 랜덤하게 가위, 바위, 보 중 하나를 선택
    # random -> 정수 (integer)
    rsp = ["가위", "바위", "보"]
    input_computer = rsp[random.randint(0, 2)] 

    msg_result = ""
    # 결과 판별 
    # 1) 무승부
    if input_user == input_computer:
        msg_result = "무승부"
        count_draw += 1
    # 2) 승
    elif input_user == "가위" and input_computer == "보" or \
        input_user == "바위" and input_computer == "가위" or \
        input_user == "보" and input_computer == "바위":
        msg_result = "승리"
        count_win += 1
    # 3) 패
    else:
        msg_result = "패"
        count_lose += 1

    # 출력
    print("사용자: ", input_user, "\t컴퓨터: ", input_computer)
    print("결과: ", msg_result)
    print(f"상태 : {count_win}승 {count_lose}패 {count_draw}무")