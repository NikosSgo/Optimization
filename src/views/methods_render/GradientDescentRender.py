from OpenGL.GL import *


class GradientDescentRender:
    def __init__(self,z_scale = 1/100):
        self.current_step = 0
        self.data = []

        self.z_scale = z_scale

    def draw(self):
        if self.data:
            """Рисуем часть пути (от начала до current_step)"""
            glColor3f(0, 0, 0)
            glLineWidth(5.0)

            glBegin(GL_LINE_STRIP)
            for i in range(self.current_step + 1):
                x, y, z = self.data[i]
                glVertex3f(x, y, z * self.z_scale)
            glEnd()

            glColor3f(1, 0, 0)
            glPointSize(8.0)
            glBegin(GL_POINTS)
            x, y, z = self.data[self.current_step]
            glVertex3f(x, y, z * self.z_scale)
            glEnd()