# 높이가 5인 다이아몬드 형태의 별을 출력

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
######################################

star = -1
space = 5
for count in range(5):
    star += 2
    space -= 1
    print(f"{space * " "}{star * "*"}")

star = 9
space = 0
for count in range(4):
    star -= 2
    space += 1
    print(f"{space * " "}{star * "*"}")