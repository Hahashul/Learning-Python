from turtle import Turtle,Screen

haha=Turtle()
Screen=Screen()

for i in range(15):
    haha.forward(10)
    haha.penup()
    haha.forward(10)
    haha.pendown()

Screen.exitonclick   