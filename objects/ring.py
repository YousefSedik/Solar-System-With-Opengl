from OpenGL.GL import glColor3f, glBegin, glEnd, glVertex3f, glNormal3f, GL_QUADS
import math


def draw_ring(cx, cy, inner_radius, outer_radius, num_segments=100):
    glColor3f(0.5, 0.5, 0.5)

    for i in range(num_segments):
        theta1 = 2.0 * math.pi * i / num_segments
        theta2 = 2.0 * math.pi * (i + 1) / num_segments

        cos_theta1 = math.cos(theta1)
        sin_theta1 = math.sin(theta1)
        cos_theta2 = math.cos(theta2)
        sin_theta2 = math.sin(theta2)

        glBegin(GL_QUADS)

        glNormal3f(cos_theta1, sin_theta1, 0)
        glVertex3f(outer_radius * cos_theta1, outer_radius * sin_theta1, 2)
        glVertex3f(outer_radius * cos_theta1, outer_radius * sin_theta1, -2)
        glVertex3f(outer_radius * cos_theta2, outer_radius * sin_theta2, -2)
        glVertex3f(outer_radius * cos_theta2, outer_radius * sin_theta2, 2)

        glNormal3f(-cos_theta1, -sin_theta1, 0)
        glVertex3f(inner_radius * cos_theta1, inner_radius * sin_theta1, 2)
        glVertex3f(inner_radius * cos_theta1, inner_radius * sin_theta1, -2)
        glVertex3f(inner_radius * cos_theta2, inner_radius * sin_theta2, -2)
        glVertex3f(inner_radius * cos_theta2, inner_radius * sin_theta2, 2)

        glNormal3f(0, 0, 1)
        glVertex3f(outer_radius * cos_theta1, outer_radius * sin_theta1, 2)
        glVertex3f(outer_radius * cos_theta2, outer_radius * sin_theta2, 2)
        glVertex3f(inner_radius * cos_theta2, inner_radius * sin_theta2, 2)
        glVertex3f(inner_radius * cos_theta1, inner_radius * sin_theta1, 2)

        glNormal3f(0, 0, -1)
        glVertex3f(outer_radius * cos_theta1, outer_radius * sin_theta1, -2)
        glVertex3f(outer_radius * cos_theta2, outer_radius * sin_theta2, -2)
        glVertex3f(inner_radius * cos_theta2, inner_radius * sin_theta2, -2)
        glVertex3f(inner_radius * cos_theta1, inner_radius * sin_theta1, -2)

        glEnd()


def init_ring_coordinates():
    coordinates = []
    inner_radius, outer_radius = 50, 52

    for i in range(7):
        coordinates.append([0, 0, inner_radius, outer_radius])
        inner_radius += 30 + i * 2
        outer_radius += 30 + i * 2
    return coordinates
