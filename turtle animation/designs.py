import turtle

def change_color():
    t.color(random.choice(["red", "yellow", "blue", "green", "purple", "orange", "cyan", "magenta"]))

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.onclick(lambda x, y: t.goto(x, y))
screen.listen()
screen.onkey(change_color, "space")

t.speed(1)
t.width(2)

turtle.done()
