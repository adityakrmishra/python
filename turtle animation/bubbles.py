import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

for _ in range(50):
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()
    t.pencolor(random.choice(["red", "yellow", "blue", "green", "purple", "orange", "cyan", "magenta"]))
    t.circle(random.randint(10, 50))

t.hideturtle()
turtle.done()
