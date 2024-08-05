# List comprehension: 리스트 내 원소를 동적으로 생성하는 방법
# 수식 for 선택항목 in 선택 리스트 if 조건식

# for else
# while else
#________________________________________

for value in range(3): # N -> N번 반복, 0 -> N-1, 3 -> 3번 반복, 0 -> 2
    
    input_value = int(input("입력 값: "))
    
    if input_value <= 0:
        done_break = True
        break
    
    print(value)

msg = "break 사용" if done_break else "break 미사용"

print("msg")

#_________________________________________

for value in range(3):
    
    input_value = int(input("입력 값: "))
    
    if input_value <= 0:
        # done_break = True
        break
    
    print(value)

else:
    msg = "break 미사용"
print("msg")

##########################################
# break
# continue
# pass (Python)
#_________________________________________
# 1. break
# 중첩 반복문은 안에서 밖으로 해석해 보라

for i in range(1, 3):
    for j in range(1, 4):
        if i == 2:
            break
        print(i, ":", j) # 1:1, 1:2, 1:3

#_____________________________
for k in range(1, 5):
    for i in range(1, 3):
        for j in range(1, 4):
            if i == 2:
                break
            print(i, ":", j)
# 1:1
# 1:2
# 1:3
# 이게 4번 반복됨
#_____________________________
# 2. continue

for k in range(1, 5):
    if k == 2:
        continue

    for i in range(1, 3):
        for j in range(1, 4):
            if i == 2:
                break
            print(i, ":", j)
# 1:1
# 1:2
# 1:3
# 이게 k=2일 때 break하지 않고 continue로 건너뛰고 3번만 반복됨
#______________________________
# 3. pass: 흐름제어문, 함수, 클래스
# pass는 중간중간 테스트를 위해 코드를 실행시킬 때 erro가 뜨지 않고 실행될 수 있게 만드는 명령어, 골격을 갖추기 위함.

value = 3
if value > 3:
    # 메뉴를 출력 -> 추후 구현해야 됨
    pass
def sum(a, b, c):
    # 3개의 값을 더한 후 반환
    # 추후 구현
    pass

##########################################
# 아래 그림을 출력

# ***
# ***
# ***
# ***
#______________________________
# 나

for row in range(4):
    for star in range(4):
        if star == 3:
            print("*" * star)
#______________________________
# 교수님

for row in range(4):
    for star in range(3):
        print("*", end = "")
    if row != 3:
        print("")