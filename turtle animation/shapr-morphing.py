import turtle

def draw_polygon(t, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

for sides in range(3, 11):
    t.clear()
    draw_polygon(t, sides, 100)
    screen.update()

t.hideturtle()
turtle.done()
