import numpy as np
from src.views.methods_render.BeesAlgorithmRender import BeesAlgorithmRender

class BeeAlgorithm:
    def __init__(self):
        # Порог для остановки алгоритма: если максимальное значение фитнеса
        # достигнуто или превышает этот порог, алгоритм прекращает работу.
        self.threshold = 1e-6
        self.logs = []  # Список для логирования этапов алгоритма

    def run(self, x_axis, y_axis, fitness, generations,
            scout_bees, selected_bees, elite_bees, neighborhood_size):
        self.logs = []
        history = []

        # Инициализация начальной популяции (разведчиков)
        population = np.column_stack((
            np.random.uniform(x_axis[0], x_axis[1], scout_bees),
            np.random.uniform(y_axis[0], y_axis[1], scout_bees)
        ))
        self.logs.append(f"Инициализация популяции: {scout_bees} разведчиков")

        for generation in range(generations):
            fitness_values = np.array([fitness(x, y) for x, y in population])
            generation_data = np.column_stack((population, fitness_values))
            sorted_generation_data = generation_data[generation_data[:, 2].argsort()[::-1]]
            history.append(sorted_generation_data)

            min_fitness = np.min(fitness_values)

            best_fitness = sorted_generation_data[-1, 2]
            best_coords = sorted_generation_data[-1, :2]
            self.logs.append(f"Поколение {generation + 1}: минимум приспособленности {best_fitness}, координаты {best_coords}")

            if min_fitness <= self.threshold:
                self.logs.append(f"Достигнута точка останова: миниму {min_fitness} <= порога {self.threshold}")
                break

            # Разделение на элитные и выбранные участки
            elite_sites = sorted_generation_data[:elite_bees]
            selected_sites = sorted_generation_data[elite_bees:elite_bees + selected_bees]
            self.logs.append(f"Элитные участки: {len(elite_sites)}, выбранные участки: {len(selected_sites)}")

            # Локальный поиск:
            # 1. Для элитных пчёл – интенсивный поиск (меньший радиус)
            elite_population = self.local_search(elite_sites, neighborhood_size * 0.5, x_axis, y_axis)
            # 2. Для выбранных пчёл – менее точный, но более широкий поиск
            selected_population = self.local_search(selected_sites, neighborhood_size, x_axis, y_axis)

            # Определяем число новых разведчиков для следующего поколения
            new_scout_count = scout_bees - len(elite_population) - len(selected_population)
            if new_scout_count < 0:
                new_scout_count = 0

            scout_population = np.column_stack((
                np.random.uniform(x_axis[0], x_axis[1], new_scout_count),
                np.random.uniform(y_axis[0], y_axis[1], new_scout_count)
            ))

            # Формирование нового поколения
            population = np.vstack((elite_population, selected_population, scout_population))

        return history

    def local_search(self, sites, neighborhood_radius, x_axis, y_axis):
        """
        Выполняет локальный поиск вокруг каждой точки.
        Каждый элемент массива sites имеет вид [x, y, fitness],
        поэтому берем первые два столбца (координаты)
        и добавляем случайное смещение в пределах neighborhood_radius.
        """
        base_points = sites[:, :2]
        perturbations = np.random.uniform(-neighborhood_radius, neighborhood_radius, size=base_points.shape)
        new_points = base_points + perturbations

        # Ограничиваем точки в пределах заданных осей
        new_points[:, 0] = np.clip(new_points[:, 0], x_axis[0], x_axis[1])
        new_points[:, 1] = np.clip(new_points[:, 1], y_axis[0], y_axis[1])

        return new_points

    def get_render(self, func, z_scale,
                   x_axis, y_axis, generations,
                   scout_bees, selected_bees, elite_bees, neighborhood_size, **kwargs):
        history = self.run(x_axis, y_axis, func.calculate, generations,
                           scout_bees,
                           selected_bees,
                           elite_bees,
                           neighborhood_size)
        bee_render = BeesAlgorithmRender()
        bee_render.z_scale = z_scale
        bee_render.scout_bees = scout_bees
        bee_render.elite_bees = elite_bees
        bee_render.selected_bees = selected_bees
        bee_render.data = history
        return bee_render
