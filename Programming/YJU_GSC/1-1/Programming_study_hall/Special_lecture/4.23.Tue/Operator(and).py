# 1 이상 30 이하의 정수 중에, 짝수이면서 5의 배수를 출력
# 내가 푼 거
for i in range(1, 31):
    if i % 2 == 0:
        if i % 5 == 0:
            print(i)

##################################################
#### and 연산자
###############

# 교수님 풀이 1
for i in range(1, 31):
    if i % 2 == 0:
        if i % 5 == 0:
            print(i)

# 교수님 풀이 2
for i in range(1, 31):
    if i % 2 == 0 and i % 5 == 0:
        print(i, "\t", end="")