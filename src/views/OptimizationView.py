import numpy as np
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt6.QtCore import Qt

from src.views.functions_render.OptimizationFunctonRender import OptimizationFunctionRender
from src.views.methods_render.GradientDescentRender import GradientDescentRender


class OptimizationView(QOpenGLWidget):
    def __init__(self):
        super().__init__()

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.x_axis = ()
        self.y_axis = ()
        self.display_axes = True
        self.display_grid = True
        self.func = OptimizationFunctionRender()
        self.method = GradientDescentRender()

        self.grid_scale = 0.5

        self.camera_pos = np.array([20.0, 20.0, 20.0])
        self.camera_speed = 1.0
        self.camera_front = np.array([-20.0, -20.0, -20.0])
        self.camera_up = np.array([0.0, 0.0, 1.0])

        self.rotation_z = 0
        self.rotation_speed = 5

        self.delay = 10000
        self.timer = None


    def initializeGL(self):
        """Инициализация OpenGL"""
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glClearColor(1, 1, 1, 1.0)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        print("OpenGL initialized.")

    def timerEvent(self, event):
        """Анимация: двигаемся по пути на один шаг вперёд"""
        if self.method.current_step < len(self.method.path) - 1:
            self.method.current_step += 1
            self.update()
        else:
            self.killTimer(self.timer)

    def _draw_axes(self):
        """Рисует оси координат и сетку в плоскости XY"""
        if self.display_axes:
            glLineWidth(8.0)
            glBegin(GL_LINES)
            glColor3f(0.5, 0.5, 0.5)
            glVertex3f(self.x_axis[0], self.y_axis[0], 0)
            glVertex3f(self.x_axis[1], self.y_axis[0], 0)

            glVertex3f(self.x_axis[0], self.y_axis[0], 0)
            glVertex3f(self.x_axis[0], self.y_axis[1], 0)

            glVertex3f(self.x_axis[0], self.y_axis[0], 0)
            glVertex3f(self.x_axis[0], self.y_axis[0], 10)
            glEnd()

    def _draw_grid(self):
        # Сетка
        if self.display_grid:
            glLineWidth(1.0)
            glColor3f(0.8, 0.8, 0.8)
            glBegin(GL_LINES)
            x = self.x_axis[0]
            while x <= self.x_axis[1]:
                glVertex3f(x, self.y_axis[0], 0)
                glVertex3f(x, self.y_axis[1], 0)
                x += self.grid_scale
            y = self.y_axis[0]
            while y <= self.y_axis[1]:
                glVertex3f(self.x_axis[0], y, 0)
                glVertex3f(self.x_axis[1], y, 0)
                y += self.grid_scale
            glEnd()

    def paintGL(self):
        """Отрисовка сцены"""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        look_at = self.camera_pos + self.camera_front
        gluLookAt(*self.camera_pos, *look_at, *self.camera_up)
        glRotatef(self.rotation_z, 0, 0, 1)

        glPushMatrix()
        self.method.draw()
        self.func.draw()

        self._draw_axes()
        self._draw_grid()

        glPopMatrix()

    def resizeGL(self, w, h):
        """Обновление матрицы проекции при изменении размера окна"""
        if h == 0:
            h = 1
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / h, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)


    #Вызывается из model
    def update_state(self,data):
        if "optimization_view" in data:
            data = data["optimization_view"]
            if "update_function" in data:
                new_states = data["update_function"]
                self.x_axis = new_states["x_axis"]
                self.y_axis = new_states["y_axis"]
                self.display_grid = new_states["display_grid"]
                self.display_axes = new_states["display_axes"]
                self.method = GradientDescentRender()
                self.func = new_states["func"]
            if "run_method" in data:
                new_states = data["run_method"]
                self.delay = new_states["delay"]
                self.method = new_states["method"]
                if self.timer:
                    self.killTimer(self.timer)
                self.timer = self.startTimer(self.delay)
            self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_W:
            self.camera_pos[1] -= self.camera_speed
        elif event.key() == Qt.Key.Key_A:
            self.camera_pos[0] += self.camera_speed
        elif event.key() == Qt.Key.Key_S:
            self.camera_pos[1] += self.camera_speed
        elif event.key() == Qt.Key.Key_D:
            self.camera_pos[0] -= self.camera_speed
        elif event.key() == Qt.Key.Key_Space:
            self.camera_pos[2] += self.camera_speed
        elif event.key() == Qt.Key.Key_Z:
            self.camera_pos[2] -= self.camera_speed

        if event.key() == Qt.Key.Key_Left:
            self.rotation_z -= self.rotation_speed
        elif event.key() == Qt.Key.Key_Right:
            self.rotation_z += self.rotation_speed

        if event.key() == Qt.Key.Key_R:
            self.method.current_step = 0
            if self.timer:
                self.killTimer(self.timer)
            self.timer = self.startTimer(self.delay)

        self.update()