import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.color("white")

for _ in range(5):
    t.forward(100)
    t.right(144)  # Star angle

turtle.done()
