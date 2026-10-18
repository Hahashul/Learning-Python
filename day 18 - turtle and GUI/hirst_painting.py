# import colorgram

# colors=colorgram.extract('day 18 - turtle and GUI/image.jpg',30)
# rgb_colors=[]

# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     tuple=(r,g,b)
#     rgb_colors.append(tuple)

# print(rgb_colors)

color_list=[ (198, 174, 118), (215, 225, 218), (222, 225, 230), (126, 36, 24), (162, 103, 57), (185, 158, 52), (6, 55, 82), (46, 34, 31), (108, 68, 85), (115, 161, 174), (22, 120, 171), (67, 152, 135), (75, 37, 47), (9, 66, 46), (88, 139, 59), (128, 39, 42), (181, 97, 80), (209, 201, 148), (142, 176, 161), (176, 156, 161), (179, 202, 183), (218, 179, 171), (31, 78, 61), (86, 142, 154), (21, 77, 98), (169, 200, 207), (149, 115, 121), (207, 181, 187)]


import turtle as t
import random

t.colormode(255)
turtle=t.Turtle()
screen=t.Screen()
turtle.speed(0)
turtle.hideturtle()

turtle.teleport(-200,-200)

x=-200
y=-200
for i in range(10):
    x=-240

    for j in range(10 ): 
        x+=40
        turtle.teleport(x,y)
        turtle.dot(20,random.choice(color_list))
        
    
    y+=40








screen.exitonclick()