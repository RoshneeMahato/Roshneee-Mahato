from turtle import Turtle, Screen
from turtle import *

timmy = Turtle()
timmy.shape("circle")
timmy.color("black")

tommy = Turtle()
tommy.shape("turtle")
tommy.color("black")


def drawRectangle(x):
    x.forward(100)
    x.left(100)
    x.forward(100)
    x.left(100)
    x.forward(100)
    x.left(100)
    x.forward(100)
    x.left(100)
    x.forward(100)
    x.left(100)
    x.forward(100)
    x.left(100)
    x.forward(100)
    x.left(100)
    x.forward(100)
    x.left(100)


def drawTriangle(x):
    x.left(80)
    x.forward(200)
    x.left(80)
    x.forward(200)
    x.left(80)
    x.forward(200)
    x.left(100)
    x.forward(200)
    x.left(100)
    x.forward(200)
    x.left(100)
    x.forward(200)


drawRectangle(timmy)
tommy.penup()
tommy.backward(100)
tommy.pendown()
tommy.color()
drawRectangle(tommy)

newScreen = Screen()
print(newScreen.canvheight)
newScreen.exitonclick()


star= Turtle()

star.right(55)
star.forward(200)

for i in range(4):
    star.right(110)
    star.forward(400)

Turtle.done()