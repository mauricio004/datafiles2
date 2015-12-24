__author__ = 'MFlores1'

import math


class Point():
    pass

class Rectangle():
    pass


def distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dsquared = dx**2 + dy**2
    return math.sqrt(dsquared)


def moveRect(box, dx, dy):
    box.corner.x = box.corner.x + dx
    box.corner.y = box.corner.y + dy

blank = Point()
blank.x = 3.0
blank.y = 4.0

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 1.0
box.corner.y = 5.0
print box.corner.x
print box.corner.y
moveRect(box, 2.0, 3.0)
print box.corner.x
print box.corner.y


def moveRect(box, dx, dy):
    box.corner.x = box.corner.x + dx
    box.corner.y = box.corner.y + dy





p1 = Point()
p1.x = 1.0
p1.y = 4.0
p2 = Point()
p2.x = 2.0
p2.y = 6.0

# print distance(p1, p2)

# def distance(x1, y1, x2, y2):
#   dx = x2 - x1
#   dy = y2 - y1
#   dsquared = dx**2 + dy**2
#   result = math.sqrt(dsquared)
#   return result