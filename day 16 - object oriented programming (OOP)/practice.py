# from turtle import Turtle,Screen
# uday=Turtle()
# print(uday) 
# uday.color("red")
# uday.shape("turtle")
# my_screen=Screen()
# uday.forward(100)  
# uday.left(90)
# uday.forward(100)
# uday.left(90)
# uday.forward(100)
# uday.left(90)
# uday.forward(100)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
table.align="l"
table.add_column("pokemon name",["pikachu","squirtle","charmander"])
table.add_column("type",["electric","water","fire"])

print(table)
