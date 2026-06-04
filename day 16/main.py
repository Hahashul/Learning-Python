from turtle import Turtle,Screen
uday=Turtle()
print(uday) 
uday.color("red")
uday.shape("turtle")
my_screen=Screen()
uday.forward(100)  
uday.left(90)
uday.forward(100)
uday.left(90)
uday.forward(100)
uday.left(90)
uday.forward(100)
print(my_screen.canvwidth)
my_screen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()