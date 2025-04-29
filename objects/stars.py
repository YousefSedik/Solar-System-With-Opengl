from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random


def draw_stars(coordinates: list[list[int]]):
    # set stars color to white
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3.0)  # Make the stars larger
    glBegin(GL_POINTS)
    for x, y, z in coordinates:
        glVertex3f(x, y, 0)
    glEnd()


# def draw_star(star, x, y, size=1):
#      # Set the position of the star


def init_coordinates(number_of_coordinates: int = 10):
    data = []
    z = random.randint(0, 1)
    for i in range(number_of_coordinates):
        x, y = random.randint(0, 1920), random.randint(0, 1080)
        data.append([x, y, z])
    return data
