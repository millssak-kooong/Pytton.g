bar = [10, 20, 30, 40]

for item in bar:
    print(item)

print("-" * 10)

for index in range(-1, -5, -1):
    print(bar[index])

# Element 원소 30을 100으로 변경
# bar[좌표] = 100
bar[2] = 100

# ----------------------------------

bar =  [10, 20, 30, 40]

bar = [0, 0, 0, 0, 0, 0]

bar = [0 for _ in range(6)]

print(bar)

bar = [0] * 6

print(bar)

# ----------------------------------

bar =  [10, 20, 30, 40]

del bar[2]
print(bar.pop(2))

# ----------------------------------

bar =  [10, 20, 30, 40]

while len(bar) > 0:
    item = bar.pop(0)
    print(item)

# ----------------------------------

bar =  [10, 20, 30, 40]

bar.insert(3, 70)
print(bar)