from OpenGL.GL import *
from OpenGL.GLU import *

class BacterialAlgorithmRender:
    def __init__(self, z_scale=1/100):
        self.current_step = 0
        self.data = []
        self.z_scale = z_scale
        self.scout_bees = 0
        self.elite_bees = 0
        self.selected_bees = 0

    def draw(self):
        if self.data:
            glColor3f(0, 0, 0)
            for i in range(len(self.data[self.current_step]) - 1):
                x, y, z = self.data[self.current_step][i]
                glPushMatrix()
                glTranslatef(x, y, z * self.z_scale)
                gluSphere(gluNewQuadric(), 0.05, 20, 20)
                glPopMatrix()

            glColor3f(1, 0, 0)
            x, y, z = self.data[self.current_step][-1]
            glPushMatrix()
            glTranslatef(x, y, z * self.z_scale)
            gluSphere(gluNewQuadric(), 0.1, 20, 20)
            glPopMatrix()
