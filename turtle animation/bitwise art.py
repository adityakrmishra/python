import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)

def draw_bitwise_art(size, iterations):
    for i in range(iterations):
        t.pencolor((i % 6) / 6, (i % 3) / 3, (i % 2) / 2)
        t.forward(i & size)
        t.right(90)

draw_bitwise_art(50, 1000)

t.hideturtle()
turtle.done()
