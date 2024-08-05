# while문을 사용하여 1~1000까지의 정수 중 3의 배수의 총합을 구하라
##############################################################
# 1. 문제의 의미에 충실

three = 1
total = 0


while 1 <= three <= 1000:
        if three % 3 == 0:
            total += three
        three += 1

print("1 ~ 1000 사이 정수 중 3의 배수의 합은:", total)

#_____________________________________________________________
# 2. 문제의 목적에 충실

three = 0
total = 0

while True:
    if three <= 1000:
        three += 3
    elif three > 1000:
        break
    total += three

print("1~1000 사이 정수 중 3의 배수의 합은:", total)