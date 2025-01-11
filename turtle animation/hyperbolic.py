import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

for theta in range(360 * 5):
    r = 200 / (1 + math.cos(math.radians(theta)))
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    t.goto(x, y)

t.hideturtle()
turtle.done()
