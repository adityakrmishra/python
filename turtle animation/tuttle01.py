import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
col = ('gold','cyan')

for i in range(300):
    t.pencolor(col[i%2])
    t.width(2)
    t.forward(i)
    t.right(89)
    t.forward(i*2)
    t.right(89)

turtle.done()