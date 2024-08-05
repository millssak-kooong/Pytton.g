# CRUD : Delete
# 원소 삭제 : 원소 한 개 삭제, 리스트 내 전체 원소 삭제
# 원소 한 개 삭제 : 3 가지 방법
# 1) del 명령어를 사용해서 해당 index의 원소를 삭제
# 2) remove 함수를 이용해서 값을 이용해서 해당 원소를 삭제
# 3) pop 함수를 이용, 해당 index의 원소를 삭제하고, 삭제된 값을 반환

bar = [10, 20, 30, 40, 50, 60]
print("before : ", bar, len(bar)) # [10, 20, 30, 40, 50, 60]

del bar[1] # del은 index 값을 찾아 삭제
print("after : ", bar, len(bar)) # [10, 30, 40, 50, 60]

#_______________________________________________________________________________

bar = [10, 50, 30, 40, 50, 60]
print("before : ", bar, len(bar)) # [10, 50, 30, 40, 50, 60]

bar.remove(50) # remove는 처음 만나는 해당 원소 값을 삭제
print("after : ", bar, len(bar)) # [10, 30, 40, 50, 60]

#_______________________________________________________________________________

bar = [10, 50, 30, 40, 50, 60]
print("before : ", bar, len(bar)) # [10, 50, 30, 40, 50, 60]

print(bar.pop(2)) # 30 / # pop은 index 값을 찾아 삭제 후 반환
print("after : ", bar, len(bar))
# [10, 50, 40, 50, 60] 5
# 30

#____________________________________________________________________________
# pop 응용
# 1 ~ 5 사이 정수 중,  중복되지 않은 정수 N개 선택

import random
n = 5
max_num = 6
# List comprehension
sample_list = [ value for value in range(1, max_num) ]
# sample_list -> [1, 2, 3, 4, 5]

random_list = []

for trial_count in range(0, n):
    random_index = random.randint(0, len(sample_list) - 1)
    random_num = sample_list.pop(random_index)
    random_list.append(random_num)    
    
print(random_list)

#_____________________________________________________________________

bar = [1, 2, 3, 4, 5, 6]
bar.clear() # 원소들만 모두 삭제
print(bar)
# []

#____________________________

foo = [1, 2, 3, 4, 5, 6]
del foo # 참조 변수 자체가 사라진다.
print(foo) # print가 없을 땐 출력 값이 없으니 erro는 아니다.
# erro 좀비메모리