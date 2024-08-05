import random

# 리스트 생성: bar(참조변수)
bar = list()

for _ in range(0, 5): # 0, 1, 2, 3, 4
    # random.randint(1, 100) -> 1 이상 100 이하의 정수 중 난수를 한 개 선택
    bar.append(random.randint(1, 100)) # random 적고 'ctrl + ,'를 입력하면 'import random'이 생성된다.

print(bar)

# 예) [90, 50, 30, 100, 20]

print( bar[4], bar[-1], bar[len(bar) - 1] )
# 마지막 원소를 부르는 2 가지 방법
# index 값을 역순으로 부르기 위해 음의 정수를 사용한다.
## 마지막 방법은 원소의 개수를 세는 len 함수를 쓴 것

#_________________________________________________

bar = [10, 20, 30]
foo = [1, 2, 3]
pos = [-1, -2, -3]

kin = pos

pos = bar

pos[-1] = 100

pos = kin
print(bar[-1], pos[-1])

#_________________________________________________

bar = [10, 20, 30, 40]

foo = bar[:10:2]

print(foo)


# slicing
# [start:stop:step띄엄띄엄보폭]
## start와 stop은 인덱스값
## start, stop, step은 생략하면 각각 0, -1, +1로 기본 인식
## stop은 out of index 되는데 교수님은 안 됨???
foo = bar[0:4:2]
print(foo)

foo = bar[:]
print(foo)

foo = bar[2:]
print(foo)

foo = bar[:3]
print(foo)

foo = bar[-1:-4] # step 생략했을 때
print(foo)

foo = bar[-1:-4:-1]
print(foo)

foo = bar[-1::-1]
print(foo)

#_________________________________________________

# 770225_3983813
# 3개로 구분해서 문자열로 저장
# 첫 번째: 생년월일 6자리 -> 770225
# 두 번째: 지역 코드값 6자리 -> 398381
# 세 번째: 패리티 체크값 1자리 -> 3

bar = [7, 7, 0, 2, 2, 5, '-', 3, 9, 8, 3, 8, 1, 3]

foo = bar [:6]
print(foo)

foo = bar [7:-1]
print(foo)

foo = bar [-1]
print(foo)