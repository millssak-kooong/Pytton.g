# 1에서 100까지의 범위 내에서 중복되지 않는 랜덤 정수를 생성 후 리스트에 저장한 후 사용자가 입력한 인덱스에 해당 값을 출력
## 랜덤 정수(1~100)의 개수 N을 입력
## 1~100 중 중복되지 않는 N개의 랜덤 숫자를 생성
## 생성된 랜덤 숫자들은 리스트에 저장
## 사용자에게 리스트에서 원하는 원소의 인덱스(0~N-1)를 입력받는다.
## 프로그램은 사용자가 선택한 인덱스에 해당하는 리스트의 원소를 출력
### print, input, random.randint, len 함수 외의 함수 사용 금지
### 중복 값 검사를 위해 not in, in 연산자 사용 금지
### N이 1 미만이거나 100 초과일 경우, 계속해서 입력을 받습니다.
### 사용자가 유효하지 않은 인덱스를 입력한 경우 에러 메시지를 출력

# 1. 랜덤 정수 개수를 입력받는다.

count_num = int(input("N값을 입력하세요(1~100): "))

for test in range(1, 101):
    count_num ??
    while True:


        if intNum < 1 or 100 < intNum:
            while True:
                int(input("N은 1~100의 정수여야합니다. 다시 입력하세요: "))
      

    

# import random
# # 1
# random_number = random.randint(1, 10)
# print("랜덤한 정수:", random_number)



# book = []


# while True:
#     title = input("What is the name of the book? If you want to stop the program, input '종료'. : ")
#     if title == "종료":
#         break
#     book.append(title)

# print("Book list: ", book)


#######################################################
######## 해설
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