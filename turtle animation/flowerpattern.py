import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

for i in range(36):
    t.pencolor(colors[i % 6])
    t.circle(100)
    t.right(10)

turtle.done()
