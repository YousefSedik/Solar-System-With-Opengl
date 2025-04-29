from objects import draw_stars, init_coordinates, draw_ring, init_ring_coordinates
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

stars_coordinates = init_coordinates(200)
ring_coordinates = init_ring_coordinates()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_stars(stars_coordinates)
    for ring in ring_coordinates:
        draw_ring(*ring)

    glutSwapBuffers()


def iterate():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1920, 0.0, 1080, 0.0, 1.0)


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    wind = glutCreateWindow(b"Solar System With OpenGL")
    glutFullScreen()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()
