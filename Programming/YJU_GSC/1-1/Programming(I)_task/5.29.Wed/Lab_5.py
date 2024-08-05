# for 문을 사용하여 아래 학생들의 성적에 대한 총합, 평균, 학생 수를 출력
# 99, 29, 30, 40, 20, 60
########################

score = [99, 29, 30, 40, 20, 60]
sum = 0
avg = 0
std = 0

for num in score:
    sum += num
    std += 1
    avg = sum / std

print(f"학생 수: {std}, 총점: {sum}, 평균: {avg}")