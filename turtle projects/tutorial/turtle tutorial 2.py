import turtle

t = turtle.Turtle()
wn = turtle.Screen()

wn.bgcolor('black')

#first is line color and second is turtle color
t.color('cyan','black')
t.hideturtle()

#fill the color
t.fillcolor('cyan')

#start fill command
t.begin_fill()
for i in range(4):
     t.fd(200)
     t.left(90)

t.end_fill()

turtle.done()