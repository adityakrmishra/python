import turtle

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

t.speed(1)
t.width(2)
t.color("white")

turtle.done()
