import turtle

def draw_leaf(t, size, depth):
    if depth > 0:
        t.forward(size)
        t.right(30)
        draw_leaf(t, size * 0.7, depth - 1)
        t.left(60)
        draw_leaf(t, size * 0.7, depth - 1)
        t.right(30)
        t.backward(size)

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.left(90)
t.color("green")

draw_leaf(t, 100, 5)

t.hideturtle()
turtle.done()
