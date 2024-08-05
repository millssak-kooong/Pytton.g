bar = [] # 리스트 생성
# []

for value in range(1,20): # 총 19회 [1 -> 19, 1 증가]
    bar.append(value) # [1, 2, 3, ..., 19]

print(bar)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

# 첫 번째 원소의 값은?
print(bar[0]) # 1

#_____________________________________

foo = []

foo.append(10)
foo.append(20)
foo.append(30)
foo.append(5)

for index in range(0, 4):
    print(foo[index])
    # 1. foo[0] -> 10
    # 2. foo[1] -> 20
    # 3. foo[2] -> 30
    # 4. foo[3] -> 5

print("foo list의 사이즈: ", len(foo)) # 4