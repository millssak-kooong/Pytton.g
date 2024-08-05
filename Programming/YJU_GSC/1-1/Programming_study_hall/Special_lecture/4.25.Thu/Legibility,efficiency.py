# 정수를 입력 받아서, 0이면 0, 0 초과이면 "양의 정수"라고 출력, 0 미만이면 "음의 정수"


num = int(input("정수 입력: "))


msg = "결과: "

if num == 0:
    print("0")
elif num > 0:
    print("양의 정수")
else:
    print("음의 정수")

#____________________________________
# 가독성과 효율성(수정할 때도 편하다)

num = int(input("정수 입력: "))


msg = "결과: "

if num == 0:
    msg += "0"
elif num > 0:
    msg += "양의 정수"
else:
    msg += "음의 정수"

print(msg)