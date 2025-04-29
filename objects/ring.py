from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math


def draw_ring(cx, cy, inner_radius, outer_radius, num_segments=100):
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)

    glBegin(GL_TRIANGLE_STRIP)
    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * i / num_segments
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)

        # Outer edge vertex
        glVertex2f(cx + outer_radius * cos_theta, cy + outer_radius * sin_theta)
        # Inner edge vertex
        glVertex2f(cx + inner_radius * cos_theta, cy + inner_radius * sin_theta)
    glEnd()


def init_ring_coordinates():
    coordinates = []
    cx, cy, inner_radius, outer_radius = 960, 540, 100, 102
    for i in range(7):
        coordinates.append([cx, cy, inner_radius, outer_radius])
        inner_radius += 50 + i * 3.5
        outer_radius += 50 + i * 3.5
    return coordinates
