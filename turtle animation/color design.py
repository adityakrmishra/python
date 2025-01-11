import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)

for i in range(100):
    t.pencolor(i / 100, 0, 1 - i / 100)
    t.forward(i * 2)
    t.right(144)

t.hideturtle()
turtle.done()
