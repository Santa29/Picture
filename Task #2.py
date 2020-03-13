from graph import *
import math
import random


def oval_with_angle(x, y, size, angle, color):
    """Function draw the oval with given angle , coordinates, size, color"""
    brushColor(color)
    penColor(color)
    angle = math.radians(angle)
    point_massive_for_oval = []
    for j in range(361):
        a = 2 * size * math.cos(j)
        b = size * math.sin(j)
        a, b = a * math.cos(angle) - b * math.sin(angle), -1 * a * math.sin(angle) + b * math.cos(angle)
        k = (a + x, b + y)
        point_massive_for_oval.append(k)
    polygon(point_massive_for_oval)
    brushColor('black')


def spots(x, y, angle, size):
    """Draw the spots on mushroom. Coordinates mus be the same as in the head function mushroom"""
    a = [[0, 0.2], [-0.7, 0.6], [0.65, - 0.4], [-1.7, 0.2], [1.1, 0.2], [-0.65, -0.65]]
    if angle == 0:
        for j in range(6):
            a[j][0], a[j][1] = x + a[j][0] * size, y + a[j][1] * size
            oval_with_angle(a[j][0], a[j][1], random.randint(10, 19) / 100 * size, angle, 'white')
    elif angle > 0:
        for j in range(6):
            a[j][0], a[j][1] = x + a[j][0] * size, y + a[j][1] * size
            length = math.pow(pow(x - a[j][0], 2) + pow(y - a[j][1], 2), 0.5)
            start_angle = math.asin((a[j][0] - x) / length)
            delta_x = length * math.sin(start_angle + math.radians(angle))
            delta_y = length * math.cos(start_angle + math.radians(angle))
            oval_with_angle(x + delta_x, y + delta_y, random.randint(10, 19) / 100 * size, angle, 'white')
    else:
        for j in range(6):
            a[j][0], a[j][1] = x + a[j][0] * size, y + a[j][1] * size
            length = math.pow(pow(x - a[j][0], 2) + pow(y - a[j][1], 2), 0.5)
            start_angle = math.asin((a[j][0] - x) / length)
            delta_x = length * math.sin(start_angle - math.radians(angle))
            delta_y = length * math.cos(start_angle + math.radians(angle))
            oval_with_angle(x + delta_x, y + delta_y, random.randint(10, 19) / 100 * size, angle, 'white')


def mushroom(x, y, angle, size):
    """Draw the mushroom. Coordinates is the right and left corners of the rectangle, which is the border of oval"""
    if angle >= 0:
        oval_with_angle(x + 2 * size * math.sin(math.radians(angle)), y + 1.5 * size, size * 0.6, angle + 90, 'white')
    else:
        oval_with_angle(x + 2 * size * math.sin(math.radians(angle)), y + 1.5 * size, size * 0.6, angle + 90, 'white')
    oval_with_angle(x, y, size, angle + math.pi / 2, 'red')
    spots(x, y, angle, size)


def first_plan(max_width, width_mushrooms, height_max):
    """Draw the line of mushrooms on the first plane"""
    for j in range(5):
        x_coord = (max_width - width_mushrooms) / 5 * j + width_mushrooms
        mushroom(x_coord, height_max, random.randint(-15, 15), random.randint(15, 50))


def spine(x, y, angle, size):
    penColor('black')
    brushColor('black')
    x1 = (x + size * math.sin(angle), y - size * math.cos(angle))
    x2 = (x + 0.1* size * math.cos(angle), y + math.sin(angle))
    points = [(x, y), x1, x2]
    polygon(points)


def hedgehog(x, y, size):
    brushColor(66, 48, 48)
    oval(x - 1.1 * size, y + 0.38 * size, x - 0.7 * size, y + 0.22 * size)
    oval(x + 1.1 * size, y + 0.38 * size, x + 0.7 * size, y + 0.22 * size)
    oval(x - size, y - 0.5 * size, x + size, y + 0.5 * size)
    oval(x - 0.9 * size, y + 0.48 * size, x - 0.5 * size, y + 0.32 * size)
    oval(x + 0.9 * size, y + 0.48 * size, x + 0.5 * size, y + 0.32 * size)
    oval(x + 0.8 * size, y + 0.2 * size, x + 1.5 * size, y - 0.2 * size)
    brushColor('black')
    oval(x + 1.45 * size, y, x + 1.52 * size, y - 0.06 * size)
    oval(x + 1.1 * size, y + 0.06 * size, x + 1.2 * size, y - 0.06 * size)
    oval(x + 1.25 * size, y - 0.16 * size, x + 1.35 * size, y - 0.04 * size)


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
first_plan(width, width / 2, height * 0.93)
hedgehog(width / 2, height / 2, 150)
run()
