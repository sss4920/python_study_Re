import turtle
import random

def screenleftclick(x,y) :
    global r, g, b
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x,y)

def screenrightclick(x,y) :
    turtle.penup()
    turtle.goto(x,y)

def screenmidclick(x,y) :
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    

pSize = 10
r, g, b = 0.0, 0.0, 0.0

turtle.title('거북이')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenleftclick,1)
turtle.onscreenclick(screenmidclick,2)
turtle.onscreenclick(screenrightclick,3)



turtle.done()
