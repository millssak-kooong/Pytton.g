# 1. computer random 3 numbers

# 1
import random
xbox = []

while len(xbox) < 3:
    for a in range(3):
        x = random.randint(0, 9) # 컴퓨터 난수
        xbox.append(x)
        
        if len(xbox) == 2: # 첫 번째 원소는 당연히 중복될 게 없으니까 두 번째부터 비교
            if xbox[1] == xbox[0]: # 순서대로 반복될 때 아직 생성되지 않은 인덱스는 코드로써 유효하지 않음 ex) 아직 xbox[2]는 불가능
                xbox.pop() # del xbox[1] = 인덱스 넘버를 삭제 # 리스트에서 특정 인덱스에 있는 요소를 삭제하고 그 값을 반환합니다. 인덱스를 지정하지 않으면 마지막 요소를 삭제합니다.
                continue
            continue
        elif len(xbox) == 3:
            if xbox[2] == xbox[1] or xbox[2] == xbox[0]:
                xbox.pop()
                continue
            else:
                print(xbox)
                break

#-----------------------------
# 2
import random
xbox = []

while True:
    for a in range(3): # 난수 3개
        x = random.randint(0, 9) # 컴퓨터 난수
        xbox.append(x)
    if xbox[0] == xbox[1] or xbox[0] ==  xbox[2]:
        del xbox[0:3] # 인덱스 0번부터 3개의 원소들을 삭제
    else:
        if xbox[1] == xbox[2]:
            del xbox[0:3]
        else:
            print(xbox)
            break

#-----------------------------
# 3 2024.06.22.토
import random
box = []

while True:
    x = random.randint(0,9)
    box.append(x)

    if len(box) == 3:
        if box[0] != box[1] and box[0] != box[2] and box[1] != box[2]:
            print(box)
            break
        else:
            del box