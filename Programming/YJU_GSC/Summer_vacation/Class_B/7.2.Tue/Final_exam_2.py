import random


def print_bingo_board(arg_list, col_num = 3):
    for index in range(len(arg_list)):
        print(arg_list[index], "\t", end="")
        
        if (index + 1)  % col_num == 0:
            print()

# N 값 입력
while True:
    N = int(input("N 값: 3 ~ 6"))
    
    if 3 <= N <= 6:
        break
    
bingo_element_num = N * N
# N X N 빙고 보드 작성: 1차원 배열, 1~36사이의 중복되지 않은 정수


bingo_board = []

while len(bingo_board) < bingo_element_num:
    
    rand_num = random.randint(1, 36)
    
    if rand_num not in bingo_board:
        bingo_board.append(rand_num)
        
        

bingo_count = 0

# # 빙고 숫자가 2미만일 경우
while bingo_count < 2:
    bingo_count = 0
    
    
    input("랜덤 넘버 생성: Press enter key!!")
    
    # 랜덤 넘버 생성 : 1 ~ 36
    rand_num = random.randint(1, 36)
    
    #빙고 보드 내 생성된 랜덤 값이 있을 경우 "*"로 변경
    for index in range(bingo_element_num):
        if bingo_board[index] == rand_num:
            bingo_board[index] = "*"
            break

    # 빙고 보드 출력
    print_bingo_board(bingo_board)

    # 빙고 검사
    # 가로 확인 알고리즘
    for row in range(N):
        for col in range(N):
            if bingo_board[col + (row * N)] != "*":
                break
        else:
            bingo_count += 1
    
    # 세로 확인 알고리즘
    for col in range(N):
        for row in range(N):
            if bingo_board[col + (row * N)] != "*":
                break
        else:
            bingo_count += 1

    # 대각선 : 왼쪽 -> 오른쪽 \
    for count in range(N):
        if bingo_board[ count * (N + 1) ] != "*":
            break
    else:
        bingo_count += 1

    # 대각선 : 오른쪽 -> 왼쪽 /
    for count in range(N):
        if bingo_board[(count + 1) * (N - 1)] != "*":
            break
    else:
        bingo_count += 1