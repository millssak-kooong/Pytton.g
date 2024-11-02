# 인공지능기초수학
## 이차방적식 계산 프로그램 만들기

import math


a = float(input("계수 a를 입력하시오.: "))
b = float(input("계수 b를 입력하시오.: "))
c = float(input("계수 c를 입력하시오.: "))

D = b**2 - 4*a*c

if D > 0 :
    x1 = (-b + math.sqrt(D)) / (2*a*c)
    x2 = (-b - math.sqrt(D)) / (2*a*c)
    print(f"두 개의 서로 다른 실근: {x1}, {x2}")
    
    
elif D == 0:
    x = -b / (2*a)
    print(f"하나의 중복 실근: {x}")

else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-D) / (2*a)
    print(f"실근 없음, 복(허)근: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i")