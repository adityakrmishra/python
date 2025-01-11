import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

def draw_radial_pattern(radius, sides):
    for _ in range(sides):
        t.circle(radius)
        t.left(360 / sides)

draw_radial_pattern(100, 12)

t.hideturtle()
turtle.done()
