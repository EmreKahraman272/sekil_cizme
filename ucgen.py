
import turtle
def ucgen_çizme(a,b,re,k):
    turtle.pencolor(re)
    turtle.pensize(k)
    for i in range(a):
        turtle.forward(b)
        turtle.left(120)
    turtle.done()
ucgen_çizme(4,100,"blue",7)