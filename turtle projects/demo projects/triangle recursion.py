import turtle

t = turtle.Turtle()
t.speed(150)
t.hideturtle()

def triangle(length,depth):
     if depth > 1:
          t.dot()
     if depth == 0:
          t.stamp()
     else:
          t.fd(length)
          triangle(length/2, depth-1)
          t.bk(length)
          t.left(120)
          t.fd(length)
          triangle(length/2, depth-1)
          t.bk(length)
          t.left(120)
          t.fd(length)
          triangle(length/2, depth-1)
          t.bk(length)
          t.left(120)

triangle(200,6)

turtle.done()