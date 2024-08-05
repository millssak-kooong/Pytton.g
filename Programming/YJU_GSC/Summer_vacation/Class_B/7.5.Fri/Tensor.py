tensor = [[[1, 2, 3], [0, 4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

print(len(tensor)) # 2
print(len(tensor[0])) # 3
print(len(tensor[0][1])) # 4

# --------------------------------

bar = [[[0 for depth in range(4)] for row in range(3)] for column in range(2)]
print(bar)