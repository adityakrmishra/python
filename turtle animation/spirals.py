import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

phi = (1 + math.sqrt(5)) / 2  # Golden ratio

for i in range(100):
    angle = i * math.pi / 12
    r = phi**i
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    t.goto(x, y)

t.hideturtle()
turtle.done()
