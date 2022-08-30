import turtle
import time

BODY_COLOR = 'RED'
BODY_SHADOW = ''
GLASS_COLOR = '#9acedc'
GLASS_SHADOW = ''

S = turtle.getscreen()
t = turtle.Turtle()

def body():

    t.pensize(20)
    t.fillcolor('BODY_COLOR')
    t.begin_fill()

    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    t.right(180)
    t.circle(100, -180)

    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    t.circle(40, -180)
    #t.right(90)
    t.left(7)
    t.backward(50)

    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    #t.right(180)
    #t.circle(25, -180)
    t.right(240)
    t.circle(50, -240)

    t.end_fill()
    time.sleep(10)