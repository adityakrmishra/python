import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)

def random_walk(t, steps, distance):
    for _ in range(steps):
        t.color(random.choice(["red", "yellow", "blue", "green", "purple", "orange", "cyan", "magenta"]))
        t.forward(distance)
        t.left(random.choice([90, -90, 180]))

random_walk(t, 200, 20)

t.hideturtle()
turtle.done()
