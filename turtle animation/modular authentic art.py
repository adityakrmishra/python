import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)

for i in range(360):
    t.goto(200 * math.sin(math.radians(i)), 200 * math.cos(math.radians(i)))
    t.right(1)

t.hideturtle()
turtle.done()
