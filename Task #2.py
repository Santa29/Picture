from graph import *


def hedgehog(x, y, size):
    pass


def light(x, y, size, invert):
    pass


def mushroom(angle, size):
    pass


width = 1600
height = 900
windowSize(width, height)
penColor(0, 0, 0)
brushColor(0, 150, 0)
print(coords(rectangle(0, 0, width, height / 3 * 2)))
penColor(0, 0, 0)
brushColor('grey')
rectangle(0, height / 3 * 2, width, height)
run()
