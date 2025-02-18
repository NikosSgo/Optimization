import numpy as np
import numdifftools as nd

from src.views.methods_render.GradientDescentRender import GradientDescentRender

class GradientDescent:
    def __init__(self):
        self.tolerance = 1e-6
        self.logs = []  # Добавляем список для логов

    def run(self, func, start_x, start_y, step, count_iterations):
        self.logs = []
        x, y = start_x, start_y
        path = [(x, y, func.calculate(x, y))]
        self.logs.append(f"Начальная точка: x={x}, y={y}, f(x, y)={func.calculate(x, y)}")

        for i in range(count_iterations):
            grad = nd.Gradient(lambda v: func.calculate(v[0], v[1]))((x, y))
            new_x, new_y = x - step * grad[0], y - step * grad[1]

            self.logs.append(f"Итерация {i + 1}: Градиент: {grad}, Новые координаты: x={new_x}, y={new_y}")

            if np.linalg.norm([new_x - x, new_y - y]) < self.tolerance:
                self.logs.append(f"Сходимость достигнута за {i+1} итераций.")
                break

            x, y = new_x, new_y
            path.append((x, y, func.calculate(x, y)))

        return path

    def get_render(self, func, z_scale, start_x, start_y, step, count_iterations, **kwargs):
        path = self.run(func, start_x, start_y, step, count_iterations)
        gradient_render = GradientDescentRender()
        gradient_render.z_scale = z_scale
        gradient_render.path = path
        return gradient_render
