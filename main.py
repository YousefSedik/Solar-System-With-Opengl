from objects import draw_stars, init_coordinates, draw_ring, init_ring_coordinates
from OpenGL.GLUT import (
    glutInit,
    glutInitDisplayMode,
    GLUT_RGBA,
    GLUT_DOUBLE,
    GLUT_DEPTH,
    glutInitWindowSize,
    glutCreateWindow,
    glutFullScreen,
    glutDisplayFunc,
    glutIdleFunc,
    glutMainLoop,
    glutSwapBuffers,
)
from OpenGL.GLU import gluPerspective, gluLookAt
from OpenGL.GL import (
    glClear,
    glLoadIdentity,
    glEnable,
    GL_DEPTH_TEST,
    GL_LIGHTING,
    GL_COLOR_BUFFER_BIT,
    GL_DEPTH_BUFFER_BIT,
    glRotatef,
)

stars_coordinates = init_coordinates(100)
ring_coordinates = init_ring_coordinates()
angle = 0


def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluPerspective(70, (1920 / 1080), 0.1, 1000.0)
    gluLookAt(0, 0, 500, 0, 0, 0, 0, 1, 0)

    glRotatef(angle, 0, 1, 0)
    angle += 0.05

    draw_stars(stars_coordinates)
    for ring in ring_coordinates:
        draw_ring(*ring)

    glutSwapBuffers()


def init():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1920, 1080)
    wind = glutCreateWindow(b"3D Solar System With OpenGL")
    glutFullScreen()
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()
