import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.penup()

for x in range(-200, 200, 20):
    for y in range(-200, 200, 20):
        t.goto(x, y)
        t.dot(5, "white")

t.hideturtle()
turtle.done()
