import colorgram
import turtle as turtle_module
import random


turtle_module.colormode(255)
tim = turtle_module.Turtle()
rgb_color = []

tim.speed("fastest")
colors = colorgram.extract('dot.jpg', 30)

color_list = [(202, 164, 109), (240, 245, 242), (236, 239, 243), (153, 75, 49), (222, 201, 136),
  (53, 94, 124), (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87),
  (73, 44, 36), (14, 97, 72), (145, 178, 148), (91, 73, 75), (233, 176, 165), (160, 143, 159),
  (54, 47, 50), (184, 205, 172), (35, 61, 75), (22, 85, 89), (146, 19, 21), (86, 146, 130),
  (38, 67, 91), (13, 72, 66), (106, 128, 155), (175, 99, 101), (176, 192, 209)]

tim.penup()
tim.hideturtle()
count = 100
tim.setheading(225)
tim.fd(300)
tim.setheading(0)
for dot_count in range(1, count + 1):
    color_rand = random.choice(color_list)
    tim.dot(20, color_rand)
    tim.fd(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

"""for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)
print(rgb_color)"""
screen = turtle_module.Screen()
screen.exitonclick()