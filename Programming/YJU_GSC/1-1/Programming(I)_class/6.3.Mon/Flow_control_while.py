# while 조건식(참일 때 실행되는 문장):

# 키보드로부터 정수를 입력받고 양수일 경우 출력
# 음수 또는 0일 경우 재입력 -> 양수가 입력될 때까지


x = int(input("put an integer num"))
while x <= 0:
    print(int(input("reput")))
    if x > 0:
        print(x)
        break

#_______________________________
# while 문으로 1 ~ 10을 출력
count = 1
while count <= 10:
    print(count)
    count += 1