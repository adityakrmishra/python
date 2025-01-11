import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Define colors
colors = ["red", "yellow", "blue", "green", "purple", "orange", "cyan", "magenta"]

# Function to draw a fractal tree
def draw_fractal_tree(t, branch_length, angle, depth):
    if depth > 0:
        t.pencolor(random.choice(colors))
        t.forward(branch_length)
        t.right(angle)

        # Recursively draw the right subtree
        draw_fractal_tree(t, branch_length - 10, angle, depth - 1)

        t.left(angle * 2)

        # Recursively draw the left subtree
        draw_fractal_tree(t, branch_length - 10, angle, depth - 1)

        t.right(angle)
        t.backward(branch_length)

# Position the turtle
t.penup()
t.goto(0, -250)
t.pendown()
t.left(90)

# Draw the fractal tree
draw_fractal_tree(t, 100, 30, 10)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
