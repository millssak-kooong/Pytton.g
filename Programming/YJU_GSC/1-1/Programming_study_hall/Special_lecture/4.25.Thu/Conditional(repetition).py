# 1부터 20까지 정수 출력

for x in range(1 ,21):
    print(x, "\t", end="")


###################################
# 내가 짠 거
x = 0

while True:
    x = x + 1
    print(x)
    if x == 20:
        break
###################################
# 교수님 답안
count = 1

while count < 21:
    print(count)
    count += 1