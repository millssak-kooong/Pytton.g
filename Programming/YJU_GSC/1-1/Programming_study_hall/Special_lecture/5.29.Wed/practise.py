# 10이상 20이하 정수 중 짝수의 합을 계산하라.

sum = 0

for value in range(10, 21, 2):
    sum += value

# for value in range(10, 21):
    
#     if value % 2 == 0:
#         sum = sum + value
        
print(sum)

for value in range(10, 21):
    if value % 2 == 0:
        sum = value + sum

#################################################
# 5단과 7단은 제외하고 출력

for dan in range(2, 10):
    if dan != 5 and dan != 7:
        for num in range(1, 10):
           print(f"{dan} X {num} = {dan * num}")

        print("----------")
#__________________________________
for dan in range(2, 10):
    if dan == 5 or dan == 7:
        continue
    for num in range(1, 10):
       print(f"{dan} X {num} = {dan * num}")

    print("----------")