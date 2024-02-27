import turtle
turtle.speed('fast')

def peano(l, n):
  if n == 0:
    turtle.forward(l)
  else:
    peano(l/3., n-1)
    turtle.left(90)
    peano(l/3., n-1)
    turtle.right(90)
    peano(l/3., n-1)
    turtle.right(90)
    peano(l/3., n-1)
    turtle.right(90)
    peano(l/3., n-1)
    turtle.left(90)
    peano(l/3., n-1)
    turtle.left(90)
    peano(l/3., n-1)
    turtle.left(90)
    peano(l/3., n-1)
    turtle.right(90)
    peano(l/3., n-1)
    
    
for n in range(6):
  peano(3**5, n)
  turtle.penup()
  turtle.back(3**5)
  turtle.pendown()