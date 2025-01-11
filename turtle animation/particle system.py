import turtle
import random

class Particle(turtle.Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.speed(0)
        self.color(random.choice(["red", "yellow", "blue", "green", "purple", "orange", "cyan", "magenta"]))
        self.goto(random.randint(-300, 300), random.randint(-300, 300))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(5)
        if abs(self.xcor()) > 300 or abs(self.ycor()) > 300:
            self.right(180)

particles = [Particle() for _ in range(50)]

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

while True:
    for particle in particles:
        particle.move()
    screen.update()
