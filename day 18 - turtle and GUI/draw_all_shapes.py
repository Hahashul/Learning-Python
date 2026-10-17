from turtle import Turtle,Screen
import random

turtle=Turtle()
Screen=Screen()
colors=[ "Green","Brown","Black","Yellow","Red","Tan","Gray","Orange","Blue"]

def draw_shape(side):
    angle=360/side
    for i in range(side):
        turtle.forward(100)
        turtle.right(angle)

for shape_side in range(3,11):
    turtle.color(random.choice(colors))
    draw_shape(shape_side)


