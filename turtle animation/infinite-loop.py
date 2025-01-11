import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

while True:
    t.pencolor((t.xcor() + t.ycor()) % 256 / 255, 1, 1)
    t.forward(10)
    t.right(91)  # Adjust this angle to change the looping pattern
