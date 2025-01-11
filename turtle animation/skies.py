import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.penup()

for _ in range(100):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    t.goto(x, y)
    t.dot(random.randint(2, 5), "white")

t.hideturtle()
turtle.done()
