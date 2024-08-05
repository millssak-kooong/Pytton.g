import random


while True:
# 1. 입력 받기
    value_board = int(input("Enter the size of the bingo board (3 to 6): "))
    if 3 <= value_board <= 6:
        print("Initial Bingo Board:\n")

# 2. 빙고 보드 생성
        xbox = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        # x = random.randint(0, 35)

        for _ in range(36):
            _ = random.randint(0, 35)
            # print(f"{xbox[_]} {xbox[_]} {xbox[_]}\n{xbox[_]} {xbox[_]} {xbox[_]}\n{xbox[_]} {xbox[_]} {xbox[_]}")

# 3. 보드 출력
    print(f"{xbox[_]} {xbox[_]} {xbox[_]}\n{xbox[_]} {xbox[_]} {xbox[_]}\n{xbox[_]} {xbox[_]} {xbox[_]}")


# 4. 난수 발생 및 게임 진행
    for n in range(1, 37):
        value_num = input(f"Press Enter to generate a random number:\nRandom Number {n}: ")


# 5. 빙고 확인
    
    # 입력값 예외 처리
    else:
        print("Size must be between 3 to 6. Please try again.")