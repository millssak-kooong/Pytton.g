print("=" * 20)
print("1. 학생 성적 입력\n2. 학생 목록 출력(입력 순)\n3. 프로그램 종료\n")
print("=" * 20)



def std_count():
    std_id = input("학번 입력: ")
    std_name = input("학생 이름: ")
    std_kor = int(input("국어 점수: "))
    std_eng = int(input("영어 점수: "))
    std_math = int(input("수학 점수: "))
    sum = std_kor + std_eng + std_math
    avg = sum / 3
    std_if[row].append(std_id)
    std_if[row].append(std_name)
    std_if[row].append(std_kor)
    std_if[row].append(std_eng)
    std_if[row].append(std_math)
    std_if[row].append(sum)
    std_if[row].append(avg)


while True:
    value = input("메뉴 선택(1 ~ 3): ")
    if value == 1:
        std_if = []
        std_if.append([])
        


# 1. 메뉴 입력
#    1번 성적 입력을 누르면 새로운 학생 정보 리스트를 만든다.
#    리스트에 정보를 넣는다.

# 2. 학생 정보 출력
#    지금까지 입력한 학생들의 정보를 출력한다.

# 3. 종료



while True:
    value = input("메뉴 선택(1 ~ 3): ")

    if value == 1:
        std_num = []
            
                

print(std_if)