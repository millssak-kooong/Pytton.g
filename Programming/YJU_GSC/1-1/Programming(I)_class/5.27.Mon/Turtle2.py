import random
import turtle

t = turtle.Turtle()
# 화면 설정
screen = turtle.Screen()
screen.title("Turtle 키보드 이벤트 처리 예제")

width = screen.window_width() // 2
heigth = screen.window_heigth() // 2

print("윈도우 가로X세로", width, heigth)
# 거북이를 생성합니다.
def move_foreard():
    t.forward(100)
    x, y = t.position()

    if x >= width: or x <= -width or y >= heigth:
        t.right(180)
    
def random_color():
    colors = ["red", "orange", "yellow", "green", "blue", "puple"]
    t.pencolor(random.choice(colors))