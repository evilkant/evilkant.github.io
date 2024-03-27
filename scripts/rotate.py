import turtle
import time
import math
import tkinter as tk

def connect_points(points, pen):
    if points:
        # Move to the starting point
        starting_point = points[0]
        pen.up()
        pen.goto(starting_point[0], starting_point[1])
        pen.down()

        # Connect all points
        for point in points[1:]:
            pen.goto(point[0], point[1])
        
        # Connect the last point to the first
        pen.goto(starting_point[0], starting_point[1])

def draw(list_of_points, pen, scale_factor=1.0, rotate_degree=0):
    for points in list_of_points:
        points = [rotate_2d(rotate_degree, point) for point in points]
        points = [scale(scale_factor, point) for point in points]
        connect_points(points, pen)

def draw_david_star(pen, scale_factor=1.0, rotate_degree=0):
    # the original david start
    tri_A = [(0, 1), (math.sqrt(3)/2, -1/2), (-math.sqrt(3)/2, -1/2)]
    tri_B = [(0, -1), (math.sqrt(3)/2, 1/2), (-math.sqrt(3)/2, 1/2)]
    list_of_points = [
        tri_A,
        tri_B
    ]

    for points in list_of_points:
        points = [rotate_2d(rotate_degree, point) for point in points]
        points = [scale(scale_factor, point) for point in points]
        connect_points(points, pen)

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)  # No animation
turtle.tracer(0, 0)  # Turn off the animation completely
pen.hideturtle()

def scale(k, vector):
    # Use a generator expression to scale each component of the vector
    return tuple(k * component for component in vector)

def rotate_2d(theta, vector):
    x, y = vector[0], vector[1]
    xx = x*math.cos(theta) - y*math.sin(theta)
    yy = x*math.sin(theta) + y*math.cos(theta)
    return (xx, yy)

try:
    # Animation loop
    theta = 0
    while True:
        theta += (math.pi/360)%(2*math.pi)
        pen.clear()  # Clear the previous drawing
        draw_david_star(pen, scale_factor=100, rotate_degree=theta)
        turtle.update()  # Update the screen with the new drawing
        time.sleep(0.01)  # Wait a second before the next frame
except turtle.Terminator:
    # This exception will be raised when the window is closed
    pass
except tk.TclError:
    pass
