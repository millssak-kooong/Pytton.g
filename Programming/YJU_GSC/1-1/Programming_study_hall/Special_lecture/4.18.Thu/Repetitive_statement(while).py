# 4.15.월 과제 Lab2 풀이



# 유효값: 1 <= trial_num <= 100
# 유효범위 이외 값인 경우 에러메시지 출력 후 재입력
import random

# 무한루프
while True:
    
    # N 값 입력
    trail_num = int(input("N값 : "))
    
    # 입력 받은 N 값이 유효범위
    if 1 <= trail_num <= 100:
        print("으아~~ 정답이야~")
        # 무한루프 탈출
        break
    
    # 에러 메시지 출력
    print("에러: 1이상 100이하 값 입력")

# 중복 값이 없는 정수의 개수




# 중복 값이 없는 정수를 저장할 List
made_list = []

# trail_num 개수 만큼 중복값이 없는 정수 생성 후 리스트에 저장
for trial_count in range(0, trail_num):
    
    # 중복 값 검사을 위해서.
    while True:
        random_num = random.randint(1, 5)
    
        found_duplication = False
        
        for made_index in range(0, trial_count):
            # 중복값이 있으면
            if made_list[made_index] == random_num:
                found_duplication = True
                break

        if not found_duplication:
            made_list.append(random_num) 
            break

print(made_list)
    
while True:
    input_index = int(input("index : "))
    
    if 0 <= input_index < len(made_list):
        print("원소 값 : ", made_list[input_index])
        break
    
    print("out of index")