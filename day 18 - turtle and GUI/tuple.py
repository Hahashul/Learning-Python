import turtle as t
import random

turtle=t.Turtle()
screen=t.Screen()
t.colormode(255)

def random_color():
    red=random.randint(0,255)
    blue=random.randint(0,255)
    green=random.randint(0,255)
    random_color=(red,blue,green)
    return random_color

turtle.width(5)
turtle.speed(0)



direction=[0,90,180,270]

for i in range(200):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.left(random.choice(direction))

screen.exitonclick()    