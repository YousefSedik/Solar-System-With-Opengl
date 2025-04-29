from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from objects import draw_stars, init_coordinates

stars_coordinates = init_coordinates(100) 
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_stars(stars_coordinates)
    glutSwapBuffers()


def iterate():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1920, 0.0, 1080, 0.0, 1.0)


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    wind = glutCreateWindow(b"Solar System With OpenGL")  # Give your window a title
    glutFullScreen()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()
