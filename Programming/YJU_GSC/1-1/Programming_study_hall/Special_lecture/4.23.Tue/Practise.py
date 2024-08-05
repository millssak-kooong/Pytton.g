# 정수 3 개를 입력 받아서 제일 큰 값을 출력하시오.

num1 = int(input("첫 번째 값을 입력하시오."))
num2 = int(input("첫 번째 값을 입력하시오."))
num3 = int(input("첫 번째 값을 입력하시오."))

max = 0

if num1 >= num2 and num1 >= num3:
    max = num1
elif num2 >= num1 and num2 >= num3:
    max = num2
else:
    max = num3

print(max)

#________________________________________________

num1 = int(input("1번"))
num2 = int(input("2번"))
num3 = int(input("3번"))

max = num1

if max < num2:
    max = num2

if max < num3:
    max = num3

print(max)

#_________________________________________

max = -1

for trial_count in range(1, 4):
    msg = str(trial_count) + "번"
    input_value = int(input)