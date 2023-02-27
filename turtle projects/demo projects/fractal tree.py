import turtle

t = turtle.Turtle()
t.left(90)
t.speed(100)

def tree(i):
     if i<10:
          t.up()
     else:
          t.down()
          t.fd(i)
          t.left(30)
          tree(3* i /4)
          t.right(60)
          tree(3 * i /4)
          t.left(30)
          t.bk(i)

for d in range(4):
     tree(100)
     t.right(90)


turtle.done()