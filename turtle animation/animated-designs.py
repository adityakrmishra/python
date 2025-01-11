import turtle
import time

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

for i in range(50):
    t.pencolor((i % 6) / 6, (i % 3) / 3, (i % 2) / 2)
    t.forward(i * 10)
    t.right(144)
    time.sleep(0.05)

t.hideturtle()
turtle.done()
