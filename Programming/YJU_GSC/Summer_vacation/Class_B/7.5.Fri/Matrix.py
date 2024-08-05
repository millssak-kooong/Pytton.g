def print_matrix(arg_list):
    for row in arg_list:
        for col in row:
            print(col, "\t", end = "")
        print()
    print("-" * 20)

matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

print_matrix(matrix)

del matrix[1][1], matrix

print_matrix(matrix)

# --------------------------------------------

def del_col(arg_list, col_num):
    for index in range(len(arg_list)):
        del arg_list[index][col_num]
    print(matrix)
matrix = [ [1, 2], [4, 5, 6], [7, 8, 9, 10] ]

del_col(matrix, 1)

# --------------------------------------------

matrix = [ [1, 2, 3], [4, 5], [6, 7] ]
matrix[2].append(100)
print(matrix)

# --------------------------------------------

matrix = [ [1, 2, 3], [4, 5], [6, 7] ]

matrix.append([8, 9, 10, 11])

print(matrix)

matrix.insert(2, [100, 200, 300])

print(matrix)