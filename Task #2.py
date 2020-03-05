from graph import *
import math


def oval_with_angle(x, y, size, angle, color):
    """Function draw the oval with given angle , coordinates, size, color"""
    brushColor(color)
    penColor(color)
    point_massive_for_oval = [(x + 2 * size * math.cos(angle), y + 2 * size * math.sin(angle))]
    for j in range(1, 361):
        k = (x + 3 * size * math.cos(j), y + size * math.sin(j))
        point_massive_for_oval.append(k)
    polygon(point_massive_for_oval)
    print(point_massive_for_oval)
    brushColor('black')


def mushroom(x, y, angle, size):
    """Draw the mushroom. Coordinates is the right and left corners of the rectangle, which is the border of oval"""
    pass


def hedgehog(x, y, size):
    pass


def light(x, y, light_width, light_height):
    """Draw the rectangle by coordinates with parameters width and height"""
    brushColor('yellow')
    rectangle(x, y, x + light_width, y + light_height)


width = 1600
height = 900
windowSize(width, height)
penColor(0, 0, 0)
brushColor(0, 150, 0)
rectangle(0, 0, width, height / 3 * 2)
penColor(0, 0, 0)
brushColor('grey')
rectangle(0, height / 3 * 2, width, height)
light(0, 0, width / 15, height / 3 * 2 + 10)
light(0 + width / 7, 0, width / 6, height - 15)
light(0.9 * width, 0, width * 0.09, 0.75 * height)
light(0.75 * width, 0, 0.1 * width, height * 0.85)
mushroom(width / 2, height / 2, 30, 15)
oval_with_angle(width / 2, height / 2, 20, 0, 'red')
run()
