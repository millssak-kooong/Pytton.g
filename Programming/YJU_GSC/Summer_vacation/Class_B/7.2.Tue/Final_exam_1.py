import random

while True:
    trial_count = int(input("100 ~ 1,000,000 정수 입력: "))

    if 100 <= trial_count <= 1000000:
        break



dice_list = [0, 0, 0, 0, 0, 0]

# trial_count 만큼 랜덤 숫자를 발생 : 1 ~ 6
for _ in range(trial_count):
    # 생성된 랜덤 값에 따른, 각 주사위 번호의 횟수를 증가
    rand_num = random.randint(1, 6)

    dice_list[rand_num - 1] += 1

max_event = -1
for index in range(6):
    if dice_list[index] > max_event:
        max_event = dice_list[index]


# 히스토그램과 확률을 계산
# 주사위 1이 나올 확률 : (E1 / trial_count) * 100
for index in range(6):
    print(("*" * int(dice_list[index] / max_event) * 10), "\t", end = "") 
    print(f"{index + 1} 번 확률 : {dice_list[index] / trial_count * 100}")

