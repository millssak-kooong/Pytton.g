# Turtle
## 기본 명령어

import turtle
screen = turtle.Screen() # 화면 생성 후 거북이가 그릴 수 있는 캔버스를 만듦
t = turtle.Turtle() # 그림을 그릴 거북이 객체를 생성함

t.speed(1) # 거북이 이동 속도 설정(1~10)
t.forward(100) # 전진 100
t.right(90) # 오른쪽 회전 90도
t.backward(200)
t.left(270)
t.penup()
t.home()
t.pendown()
t.left(90)
t.forward(100)

turtle.done()