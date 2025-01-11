import turtle
import random

def draw_landscape(t):
    t.penup()
    t.goto(-400, 0)
    t.pendown()
    for _ in range(80):
        t.color(random.choice(["green", "brown", "grey"]))
        t.begin_fill()
        height = random.randint(50, 150)
        t.left(90)
        t.forward(height)
        t.right(45)
        t.forward(height / 2)
        t.right(90)
        t.forward(height / 2)
        t.right(45)
        t.forward(height)
        t.left(90)
        t.end_fill()
        t.penup()
        t.forward(10)
        t.pendown()

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)

draw_landscape(t)

t.hideturtle()
turtle.done()
