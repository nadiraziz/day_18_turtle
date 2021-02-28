import random
from turtle import *

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
direction = [0, 90, 180, 270]

nad = Turtle()

color = random.choice(colors)
nad.pensize(10)
nad.speed("fastest")

for i in range(200):
    nad.forward(30)
    nad.setheading(random.choice(direction))
    color = random.choice(colors)
    nad.color(color)

