# 1 ~ 20까지 정수 출력

for value in range(1, 21):
    #  3의 배수도 아니고 짝수도 아닌 수만 출력
    if value % 3 != 0 and value % 2 != 0:
        print(value)