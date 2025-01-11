import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)

colors = ["red", "yellow", "blue", "green", "purple", "orange", "cyan", "magenta"]
for i in range(100):
    t.pencolor(colors[i % 8])
    t.circle(i * 2, 90)
    t.right(45)

t.hideturtle()
turtle.done()
