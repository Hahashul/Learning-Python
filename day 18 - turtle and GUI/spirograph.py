import turtle as t
import random
turtle= t.Turtle()
screen = t.Screen()
t.colormode(255)

def random_color():
    red=random.randint(0,255)
    blue=random.randint(0,255)
    green=random.randint(0,255)
    color=(red,blue,green)
    return color

turtle.speed(0)

def spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading()+size_of_gap)
        
spirograph(5)

screen.exitonclick()