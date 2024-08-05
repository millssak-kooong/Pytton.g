# For문을 사용하여 5 개의 정수를 키보드로부터 입력 받아, 합계와 평균을 출력하는 프로그램 작성

# 1. 5개의 정수를 입력 받는다
sum = 0
for five in range(5):
    num = int(input(f"{five + 1}번째 값을 입력"))
    sum += num

# 2. 입력 받은 정수 값들의 합계를 계산

print(f"합계 : {sum}")

# 3. 입력 받은 정수 값들의 평균을 계산

print(f"평균 : {float(sum / 5)}")

##############################################################
# 교수님 풀이

# input_num = 5

# sum = 0
# avg = 0.0

# for trial_count in range(1, input_num + 1):
#     msg = str(trial_count) + "번째 입력 : "
#     input_value = int(input(msg))
    
#     sum = sum + input_value
    
# avg = sum / input_num

# print(sum, avg)