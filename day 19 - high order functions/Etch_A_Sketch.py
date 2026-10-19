from turtle import Turtle,Screen

tim = Turtle()
screen= Screen()

def forward():
    tim.forward(10)

def left():
    tim.left(15)

def right():
    tim.right(15)

def backward():
    tim.backward(10)   

def clear():
    
    tim.reset()


screen.listen()
screen.onkey(forward,"w")
screen.onkey(backward,"s")
screen.onkey(left,"a")
screen.onkey(right,'d')
screen.onkey(clear,'c')
screen.exitonclick()
