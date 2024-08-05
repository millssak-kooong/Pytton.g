# 다음과 같이 출력되는 프로그램 작성
## for 또는 while문 사용

# 1. while 사용하여 코드 작성
# x = 5
# space = " "
# count = [1, 2, 3, 4, 5]

# while True:
#     draw = print(f"{space * (x - 5)}{count[x - 1]}")

#     if draw == "*":
#         break
    
    # star = count[-1:-6:-1]
    # print(star)
    # if count[0]:
    #     break







##################################
# 2. for 사용하여 코드 작성

for i in range(5, 0, -1):
    star = i * "*"
    space = " " * (5 - i)
    print(f"{space}{star}")
    # print(space, star)를 하면 space와 star 사이의 공백이 생긴다.

#### 또 다른 방법 ####
# for num in range(1, 6):
#     star = (6 - num) * "*"
#     space = (num - 1) * " "
#     print(f"{space}{star}")