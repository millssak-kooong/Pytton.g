# 방향 명령어 해석기


# 1. 사용자로부터 "left", "right", "up", "down" 중 하나의 단어를 입력받습니다.

dir = input("방향을 입력하세요(left, right, up, down): ")

# 2. 입력받은 문자열에 따라 "왼쪽으로 이동합니다", "오른쪽으로 이동합니다", "위로 이동합니다", "아래로 이동합니다"를 출력하는 프로그램을 작성

if dir == "left": # 왼쪽으로 입력 받았을 때 이동하는 메세지를 출력
    print("왼쪽으로 이동합니다.")

elif dir == "right": # 오른쪽으로 입력 받았을 때 이동하는 메세지를 출력
    print("오른쪽으로 이동합니다.")

elif dir == "up": # 위쪽으로 입력 받았을 때 이동하는 메세지를 출력
    print("위로 이동합니다.")

elif dir == "down": # 아래쪽으로 입력 받았을 때 이동하는 메세지를 출력
    print("아래로 이동합니다.")

# 3. 만약 다른 단어가 입력되면 "알 수 없는 명령입니다"를 출력

else:
    print("알 수 없는 명령입니다.")