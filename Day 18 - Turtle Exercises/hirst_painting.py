# import random
# import colorgram
# import turtle as t

# colors = colorgram.extract('image.jpg', 30)


# list_of_rgb = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     list_of_rgb.append((red, green, blue))

# print(list_of_rgb)
import random
import turtle as t
t.colormode(255)

color_list = [(203, 172, 108), (220, 227, 234), (237, 245, 242), (153, 180, 195), (152, 186, 174), (193, 161, 176), (214, 203, 113), (208, 179, 195),
              (174, 188, 213), (161, 213, 187), (161, 203, 215), (114, 123, 186), (177, 160, 71), (213, 182, 181), (198, 207, 46), (105, 114, 142), (164, 121, 51)]

timmy = t.Turtle()

for line in range(-250, 250, 50):
    for column in range(-250, 250, 50):
        timmy.penup()
        timmy.pencolor(random.choice(color_list))
        timmy.setpos(column, line)
        timmy.dot(20)


screen = t.Screen()
screen.exitonclick()
