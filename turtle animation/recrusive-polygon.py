import turtle

def draw_polygon(t, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def recursive_polygons(t, sides, length, depth):
    if depth > 0:
        draw_polygon(t, sides, length)
        for _ in range(sides):
            t.forward(length)
            t.left(360 / sides)
            recursive_polygons(t, sides, length / 2, depth - 1)

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

recursive_polygons(t, 6, 100, 3)

t.hideturtle()
turtle.done()
