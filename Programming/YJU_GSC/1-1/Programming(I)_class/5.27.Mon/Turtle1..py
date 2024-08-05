import random
import turtle

screen = turtle.Screen()
screen.title("Turtle 키보드 이벤트 처리 예제")

t = turtle.Turtle()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

def change_color_to_black():
    t.pencolor("black")

def change_color_to_red():
    t.pencolor("red")

def move_random():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.pencolor(random.choice(colors))

def move_forward():
    t.forward(10)

##########################################
# i를 누르면 색깔 빨간색 -> 검은색 또는 빨간색 -> 빨간색
# 현재 팬 색깔이 검은색 또는 빨간색일 때만 변경
# 그 외 색일 때는 아무 것도 하지 말것(그래서 'else'를 못 쓴다)
def inverse_color():
    current_pen_color = t.pencolor()
    
    if current_pen_color == "red":
        t.pencolor("black")
    
    elif current_pen_color == "black":
        t.pencolor("red")
##########################################
def change_color():
    print("색깔 선택: ")
    print("1. 파란색")
    print("2. 검정색")
    print("3. 노란색")
    while True:
        input_value = int(input("숫자 입력: "))
        if 1 <= input_value <= 3:
            if input_value == 1:
                t.pencolor("blue")
            elif input_value == 2:
                t.pencolor("black")
            elif input_value == 3:
                t.pencolor("yellow")
            break
changecolor = change_color()
print(changecolor)
##########################################
def move_forward():
    t.forward(100)

    x, y = t.position()
    print(x, y)

def move_backward():
    t.backward(100)

    x, y = t.position()
    print(x, y)
##########################################

screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_random, "c")
screen.onkey(change_color_to_black, "b")
screen.onkey(change_color_to_red, "r")

screen.mainloop()