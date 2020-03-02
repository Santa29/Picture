from graph import *


def ufo(x, y, size):
    pass


def alien(x, y, size, invert):
    pass


def sky():
    pass


width = 1600
height = 900
windowSize(width, height)
penColor(0, 0, 0)
brushColor(25, 25, 112)
print(coords(rectangle(0, 0, width, height / 3 * 2)))
penColor(0, 0, 0)
brushColor(0, 100, 0)
rectangle(0, height / 3 * 2, width, height)
brushColor('white')
circle(width / 2, height / 3, 150)
run()
