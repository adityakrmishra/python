import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

for i in range(360):
    t.pencolor((i % 6) / 6, (i % 3) / 3, (i % 2) / 2)
    t.forward(i * 2)
    t.right(121)  # Adjust the angle for different looping effects

t.hideturtle()
turtle.done()
