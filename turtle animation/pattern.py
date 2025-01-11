import turtle
import numpy as np

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

n = 100  # Number of points
frequencies = np.fft.fftfreq(n)
spectrum = np.fft.fft(np.sin(np.linspace(0, 4 * np.pi, n)))

for i, freq in enumerate(frequencies):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(np.angle(spectrum[i], deg=True))
    t.forward(np.abs(spectrum[i]))

t.hideturtle()
turtle.done()
