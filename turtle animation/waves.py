import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

for x in range(-360, 360):
    y = 100 * math.sin(math.radians(x))
    t.goto(x, y)
    t.pendown()

t.hideturtle()
turtle.done()
