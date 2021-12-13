from turtle import Turtle, Screen
import random
lin = Turtle()
screen = Screen()
screen.screensize(250, 250)
screen.colormode(255)

color_list = [(199, 175, 117), (212, 222, 215), (125, 36, 24), (167, 106, 56), (186, 159, 52), (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174), (63, 153, 138), (39, 36, 35), (76, 40, 48), (9, 68, 47), (90, 141, 52), (182, 96, 79), (131, 38, 41), (141, 171, 156), (210, 200, 149), (179, 201, 186), (173, 153, 159), (212, 183, 176), (151, 114, 119)]
lin.penup()
lin.speed("fastest")
lin.hideturtle()
def circle():
    for _ in range(10):
        lin.dot(20, random.choice(color_list))
        lin.begin_fill()
        lin.end_fill()
        lin.penup()
        lin.forward(50)
        lin.pendown()

a = -250
b = -250
lin.goto(a, b)
paint = True
while paint:
    circle()
    lin.penup()
    b += 50
    lin.goto(a, b)
    if b > 200:
        paint = False

screen.exitonclick()