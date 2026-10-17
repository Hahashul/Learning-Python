from turtle import Turtle,Screen
import random

turtle=Turtle()
screen=Screen()

turtle.width(5)
turtle.speed(0)

colors=[ "Green","Yellow","Red","Tan","Orange","Blue"]

direction=[0,90,180,270]

for i in range(200):
    turtle.color(random.choice(colors))
    turtle.forward(30)
    turtle.left(random.choice(direction))

screen.exitonclick()    