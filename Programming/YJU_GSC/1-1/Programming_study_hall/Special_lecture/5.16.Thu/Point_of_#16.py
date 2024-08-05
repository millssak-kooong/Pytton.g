# 야구 문제를 풀기 위한 핵심 알고리즘 강의
# 중복되지 않은 1~10사이 정수 3개 생성
# in, not in, list 내 중복되지 않은 랜덤 정수 생성 함수 사용금지

# 3 7 4 : computer
# 2 3 4 : user
# result : 1 strike, 1 ball

import random


def getRandValue():
    rand_list = list()

    count = 0

    while count < 3:
        rand_value = random.randint(1, 10)
        found_duplicated_value = False
        
        for sub_count in range(count):
            # 중복 값이 있을 경우
            if rand_value == rand_list[sub_count]:
                found_duplicated_value = True
                break
        
        if not found_duplicated_value:
            rand_list.append(rand_value)
            count += 1
            
    return rand_list


com_list = getRandValue()
print(com_list)
    
com_list = getRandValue()
print(com_list)

com_list = getRandValue()
print(com_list)

com_list = getRandValue()
print(com_list)

com_list = getRandValue()
print(com_list)