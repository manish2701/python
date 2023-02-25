import turtle

t = turtle.Turtle()

#circle(radius,extent,steps)
#extent = how much degree rotation if 180 the semicircle
#steps = no of vertices

t.fillcolor('cyan')

t.begin_fill()

t.circle(100,steps = 3)
t.circle(75)

t.end_fill()

turtle.done()