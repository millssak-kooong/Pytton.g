# bar = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(bar[2][0])

# #----------------------------------------

# row = 3
# col = 4

# matrix = [[0 for _ in range(col)] for _ in range(row)]
# print(matrix)

# matrix = [[0] * 4 for _ in range(3)]
# print(matrix)

#----------------------------------------

# bar = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]

# # 'bar' Matrix의 모든 원소를 순회
# for col in bar: # 각 'col'는 'bar'의 한 행을 나타낸다.
#     for item in col: # 'col'의 각 요소(즉, 각 열의 값)를 'item'으로 순회
#         # 현재 'item'을 출력하고, 같은 행의 다른 아이템과 공백으로 구분
#         print(item, end = ' ')
#     print()

#############################################
# Lab 2

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))


matrix = [[] for _ in range(row)]
print(matrix)


for x in range(row):    
    for y in range(column):
        value = input(f"Enter value for {[x]}{[y]}: ")
        matrix[x].append(value)

for a in matrix:
    for b in a:
        print(b, end = " ")
    print()