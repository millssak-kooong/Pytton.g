# n = 5


# for x in range(n): # n : 0 -> 4 (총 5회 반복)
#     for x in range(n): # n : 0 -> 4 (총 5회 반복)
#         print("*", end="")
#     print()

########################################

# # n = 5
# count = 5
# for x in range(0, 5): # 세로로 5번 반복
#     for x in range(count): # 가로로 한 개씩 줄어든다
#         print("*", end="")
#     count -= 1 # 같은 방법: count += -1
#     print()

########################################

# row_count = 5
# blank_count = row_count - 1
# star_count = 1

# for x in range(row_count): # 세로 5번

#     for x in range(blank_count):
#         print(" ",end = "")
    
#     for x in range(star_count):
#         print("*", end = "")
    
#     print()
#     blank_count -= 1
#     star_count += 1

########################################

row_count = 5
blank_counts = row_count - 1
star_count = 1

for _ in range(row_count):

    for _ in range(blank_counts):
        print(" ", end = "")
    blank_counts -= 1

    for _ in range(star_count):
        print("*", end = "")
    star_count += 2
    print()