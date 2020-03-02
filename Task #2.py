from graph import *


def hedgehog(x, y, size):
    pass


def mushroom(angle, size):
    pass


def light(x, y, light_width, light_height):
    brushColor('yellow')
    rectangle(x, y, light_width, light_height)


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
run()
