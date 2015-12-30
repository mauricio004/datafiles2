__author__ = 'MFlores1'

import turtle


def draw_square(some_turtle, forward_distance=100, angle=90):
    for i in range(1, 5):
        some_turtle.forward(forward_distance)
        some_turtle.right(angle)


def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    # Create turtle brad - draw a square
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(50)
    draw_square(brad)
    for i in range(1, 100):
        brad.right(5)
        draw_square(brad)
    # Create the turtle angie - draw a circle
    # angie = turtle.Turtle()
    # angie.shape('arrow')
    # angie.color('blue')
    # angie.circle(100)

    window.exitonclick()

draw_art()
