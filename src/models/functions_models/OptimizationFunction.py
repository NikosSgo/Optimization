from abc import ABC, abstractmethod
from src.views.functions_render.OptimizationFunctonRender import OptimizationFunctionRender
import numpy as np

class OptimizationFunction():
    def __init__(self):
        self.step = 0.5

    def calculate_data(self,x_axis,y_axis):
        """Вычисление данных для отрисовка"""
        surface = []

        for x in np.arange(x_axis[0], x_axis[1], self.step):
            for y in np.arange(y_axis[0], y_axis[1], self.step):
                z1 = self.calculate(x, y)
                z2 = self.calculate(x + self.step, y)
                z3 = self.calculate(x + self.step, y + self.step)
                z4 = self.calculate(x, y + self.step)

                surface.append((x,y,z1,z2,z3,z4))

        return surface

    def calculate(self, x, y):
        print("Should be implemented in child classes.")
        return 0

    def get_render(self,x_axis,y_axis, z_scale):
        data = self.calculate_data(x_axis,y_axis)
        function_render = OptimizationFunctionRender()
        function_render.data = data
        function_render.z_scale = z_scale
        return function_render
