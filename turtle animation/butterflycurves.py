import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

for theta in range(360 * 5):
    r = math.exp(math.cos(math.radians(theta))) - 2 * math.cos(4 * math.radians(theta)) + math.pow(math.sin(math.radians(theta / 12)), 5)
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    t.goto(x * 50, y * 50)

t.hideturtle()
turtle.done()
