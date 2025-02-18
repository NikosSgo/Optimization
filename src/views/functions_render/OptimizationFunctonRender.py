from OpenGL.GL import *

class OptimizationFunctionRender:
    def __init__(self, z_scale = 1/100, color_gradient = 6, opacity = 0.5):
        self.z_scale = z_scale
        self.color_gradient = color_gradient
        self.opacity = opacity

        self.data = []
        self.step = 0.5

    def color_alpha(self,z):
        r = z / self.color_gradient
        return (r, 0.3, 1 - r, self.opacity)

    def draw(self):
        """Отрисовка поверхности функции"""
        if self.data:
            #Отрисовка квадратов
            glBegin(GL_QUADS)
            for x,y,z1,z2,z3,z4 in self.data:
                    z1 *= self.z_scale
                    z2 *= self.z_scale
                    z3 *= self.z_scale
                    z4 *= self.z_scale

                    glColor4f(*self.color_alpha(z1))
                    glVertex3f(x, y, z1)

                    glColor4f(*self.color_alpha(z2))
                    glVertex3f(x + self.step, y, z2)

                    glColor4f(*self.color_alpha(z3))
                    glVertex3f(x + self.step, y + self.step, z3)

                    glColor4f(*self.color_alpha(z4))
                    glVertex3f(x, y + self.step, z4)
            glEnd()