import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

for i in range(36):
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

t.hideturtle()
turtle.done()
