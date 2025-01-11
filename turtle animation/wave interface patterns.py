import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

def draw_wave(amplitude, frequency, phase_shift):
    t.penup()
    for x in range(-360, 360):
        y = amplitude * math.sin(math.radians(frequency * x) + phase_shift)
        t.goto(x, y)
        t.pendown()

for i in range(3):
    draw_wave(100, 1, i * 2 * math.pi / 3)

t.hideturtle()
turtle.done()
