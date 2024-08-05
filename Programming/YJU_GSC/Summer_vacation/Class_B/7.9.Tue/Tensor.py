bar = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]\
       , [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# [2][3][4]으로 구성
# 3 X 3 Matrix가 2 장


# 첫 번째: 1번 째 Matrix가 반환
# 두 번째: 2번 째 Matrix가 반환

for matrix in bar:
    # print(matrix)
    for row in matrix:
        # print(row)
        for column in row:
            print(column, "\t", end = "")
        print()
    print("-" * 20)