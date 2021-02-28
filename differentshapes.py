from turtle import *
import random

tim = Turtle()
colors  = ["red","green","blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from


def shape(edge):
    for i in range(edge):
        angle = 360 / edge
        tim.fd(80)
        tim.rt(angle)


for i in range(3, 11):
    shape(i)
    color = random.choice(colors)
    tim.color(color)


screen = Screen()
screen.exitonclick()