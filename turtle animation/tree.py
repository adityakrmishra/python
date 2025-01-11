import turtle

def draw_branch(t, branch_length, angle):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(angle)
        draw_branch(t, branch_length - 15, angle)
        t.left(2 * angle)
        draw_branch(t, branch_length - 15, angle)
        t.right(angle)
        t.backward(branch_length)

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.color("green")
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -200)
t.pendown()

draw_branch(t, 100, 30)

turtle.done()
