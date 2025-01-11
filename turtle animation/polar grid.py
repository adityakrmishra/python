import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

for i in range(12):
    t.circle(100)
    t.right(30)

t.hideturtle()
turtle.done()
