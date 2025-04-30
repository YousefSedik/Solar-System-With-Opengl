from OpenGL.GL import (
    glColor3f,
    glBegin,
    glEnd,
    glVertex3f,
    glPointSize,
    glDisable,
    GL_LIGHTING,
    GL_POINTS,
    glEnable,
)
import random
import math


def draw_stars(coordinates: list[list[float]]):
    glColor3f(1.0, 1.0, 1.0)
    glDisable(GL_LIGHTING)
    for x, y, z, size in coordinates:
        glPointSize(size)
        glBegin(GL_POINTS)
        glVertex3f(x, y, z)
        glEnd()
    glEnable(GL_LIGHTING)


def init_coordinates(number_of_coordinates: int = 10):
    data = []
    for i in range(number_of_coordinates):
        theta = random.uniform(0, 2 * 3.14159)
        phi = random.uniform(0, 3.14159) 
        radius = random.uniform(200, 1000)

        x = radius * math.sin(phi) * math.cos(theta)
        y = radius * math.sin(phi) * math.sin(theta)
        z = radius * math.cos(phi)
        size = random.uniform(2, 3)
        data.append([x, y, z, size])
    return data
