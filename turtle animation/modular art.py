import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

for i in range(60):
    t.pencolor(colors[i % 6])
    t.circle(i * 5)
    t.right(60)

t.hideturtle()
turtle.done()
