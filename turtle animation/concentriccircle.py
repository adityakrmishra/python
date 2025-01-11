import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.color("cyan")

for i in range(10, 100, 10):
    t.penup()
    t.goto(0, -i)
    t.pendown()
    t.circle(i)

turtle.done()
