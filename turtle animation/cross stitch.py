import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

for x in range(-200, 200, 20):
    for y in range(-200, 200, 20):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(10)
        t.backward(20)
        t.forward(10)
        t.left(90)
        t.forward(10)
        t.backward(20)
        t.forward(10)
        t.right(90)

t.hideturtle()
turtle.done()
