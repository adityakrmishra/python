import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)

turtle.done()
