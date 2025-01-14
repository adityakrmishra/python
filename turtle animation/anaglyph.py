import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t1.speed(0)
t2.speed(0)
t1.pencolor("red")
t2.pencolor("cyan")

def draw_spiral(t):
    for i in range(200):
        t.forward(i)
        t.left(59)

t1.penup()
t2.penup()
t1.goto(-10, 0)
t2.goto(10, 0)
t1.pendown()
t2.pendown()

draw_spiral(t1)
draw_spiral(t2)

t1.hideturtle()
t2.hideturtle()
turtle.done()
