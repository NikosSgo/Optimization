import numpy as np
from src.views.methods_render.BacterialAlgorithmRender import BacterialAlgorithmRender

class BacterialAlgorithm:
    def __init__(self):
        self.logs = []

    def run(self, x_axis, y_axis, population_size, generations, fitness, step_size, swim_length, probability):
        self.logs = []
        history = []

        # Инициализация популяции бактерий
        population = np.column_stack((
            np.random.uniform(x_axis[0], x_axis[1], population_size),
            np.random.uniform(y_axis[0], y_axis[1], population_size)
        ))
        self.logs.append(f"Инициализация {population_size} бактерий")

        for generation in range(generations):
            fitness_values = np.array([fitness(x, y) for x, y in population])
            generation_data = np.column_stack((population, fitness_values))

            sorted_generation = generation_data[generation_data[:, 2].argsort()]
            history.append(sorted_generation)

            # Логируем лучшую бактерию
            best_fitness = sorted_generation[-1, 2]
            best_coords = sorted_generation[-1, :2]
            self.logs.append(f"Поколение {generation + 1}: максимум приспособленности {best_fitness}, координаты {best_coords}")

            # Хемотаксис (движение бактерий по градиенту)
            population = self.chemotaxis(population, fitness, step_size, swim_length, x_axis, y_axis)

            # Размножение (лучшие бактерии делятся)
            population = self.reproduction(population, fitness)

            # Элиминация-дисперсия (удаление части бактерий и замена новыми)
            population = self.elimination_dispersal(population, x_axis, y_axis, probability)

        return history

    def chemotaxis(self, population, fitness, step_size, swim_length, x_axis, y_axis):
        new_population = []

        for bacterium in population:
            direction = np.random.uniform(-1, 1, size=2)
            best_position = bacterium.copy()
            best_fitness = fitness(*bacterium)

            for _ in range(swim_length):
                new_position = best_position + step_size * direction
                new_position = np.clip(new_position, [x_axis[0], y_axis[0]], [x_axis[1], y_axis[1]])

                new_fitness = fitness(*new_position)
                if new_fitness > best_fitness:
                    best_fitness = new_fitness
                    best_position = new_position
                else:
                    direction = np.random.uniform(-1, 1, size=2)  # Меняем направление

            new_population.append(best_position)

        return np.array(new_population)

    def reproduction(self, population, fitness):
        fitness_values = np.array([fitness(x, y) for x, y in population])
        sorted_indices = np.argsort(fitness_values)[::-1]  # Отбор лучших
        top_half = population[sorted_indices[:len(population) // 2]]
        return np.vstack((top_half, top_half))  # Удваиваем лучших

    def elimination_dispersal(self, population, x_axis, y_axis, probability):
        for i in range(len(population)):
            if np.random.rand() < probability:
                population[i] = [
                    np.random.uniform(x_axis[0], x_axis[1]),
                    np.random.uniform(y_axis[0], y_axis[1])
                ]
        return population

    def get_render(self, func, z_scale, x_axis, y_axis, population_size, generations, step_size, swim_length, probability, **kwargs):
        history = self.run(x_axis, y_axis, population_size, generations, func.calculate, step_size, swim_length, probability)
        render = BacterialAlgorithmRender()
        render.z_scale = z_scale
        render.data = history
        return render
