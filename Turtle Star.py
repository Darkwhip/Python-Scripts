import turtle
t=turtle.Pen()
turtle.bgcolor('black')
t.pencolor('grey')
t.width(1)
step=10
t.forward(300)
t.backward(600)
t.fd(300)
t.left(90)
t.forward(300)
t.backward(600)
j=300
for i in range(step, 300+step, step):
    t.goto(i, 0)
    t.goto(0, j)
    t.goto(-i, 0)
    t.goto(0, -j)
    j=j-step
    t.goto(0, -j)
