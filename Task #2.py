from graph import *
import math


def hedgehog(x, y, size):
    pass


def mushroom(x, y, angle, size):
    """Draw the mushroom. Coordinates is the right and left corners of the rectangle, which is the border of oval"""
    brushColor("red")
    circle(x, y, size)
    y_right_top = y - size * math.sin(angle)
    y_left_top = y + size * math.sin(angle)
    x_left = x - 2 * size
    x_right = x + 2 * size
    circle(x_right, y_right_top, size)
    circle(x_left, y_left_top, size)
    penColor('red')
    point1 = (x_right, y_right_top + size)  # Points to draw the rectangle
    point2 = (x_left, y_left_top + size)
    point3 = (x_left, y_left_top - size)
    point4 = (x_right, y_right_top - size)
    polygon([point1, point2, point3, point4])
    penColor('black')


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
run()
