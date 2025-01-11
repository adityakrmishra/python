import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)

planets = [{"distance": 100, "speed": 1}, {"distance": 200, "speed": 0.5}, {"distance": 300, "speed": 0.25}]
for planet in planets:
    t.penup()
    t.goto(planet["distance"], 0)
    t.pendown()
    for _ in range(360):
        t.pencolor("white")
        t.forward(planet["distance"])
        t.circle(planet["distance"], planet["speed"])
    t.penup()
    t.goto(0, 0)
    t.pendown()

t.hideturtle()
turtle.done()
