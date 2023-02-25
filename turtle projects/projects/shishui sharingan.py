import turtle

t = turtle.Turtle()

t.hideturtle()

t.up()
t.goto(0,-200.5)
t.down()
t.color('red')
t.fillcolor('red')
t.begin_fill()
t.circle(200.5)
t.end_fill()

t.left(90)

t.begin_fill()
t.fillcolor('black')
t.color('black')

for i in range(4):
     t.fd(80)
     t.left(75)
     t.circle(-429,31.6)
     t.right(133.3)

t.end_fill()

t.goto(30,0)

t.fillcolor('red')
t.color('red')
t.begin_fill()
t.circle(30)
t.end_fill()

t.up()
t.goto(15,0)
t.fillcolor('black')
t.color('black')
t.begin_fill()
t.down()
t.circle(15)
t.end_fill()

turtle.done()