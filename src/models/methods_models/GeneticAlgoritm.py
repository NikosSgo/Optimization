import numpy as np
import numdifftools as nd

from src.views.methods_render.GeneticAlgorithmRender import GeneticAlgorithmRender

class GeneticAlgorithm:
    def __init__(self):
        self.tolerance = 1e-6
        self.logs = []  # Добавляем список для логов

    def run(self, x_axis, y_axis, population_size, generations, fitness):
        self.logs = []
        history = []
        population = np.column_stack((
            np.random.uniform(x_axis[0], x_axis[1], population_size),
            np.random.uniform(y_axis[0], y_axis[1], population_size)
        ))
        self.logs.append(f"Инициализация популяции: размер {population_size}")

        for generation in range(generations):
            fitness_values = np.array([fitness(x, y) for x, y in population])
            generation_data = np.column_stack((population, fitness_values))
            sorted_generation_data = generation_data[generation_data[:, 2].argsort()[::-1]]  # Сортировка по убыванию z
            history.append(sorted_generation_data)

            # Логируем лучшую бактерию
            best_fitness = sorted_generation_data[-1, 2]
            best_coords = sorted_generation_data[-1, :2]
            self.logs.append(f"Поколение {generation + 1}: минимум приспособленности {best_fitness}, координаты {best_coords}")

            if np.min(fitness_values) < self.tolerance:
                self.logs.append(f"Достигнута точка останова: минимум ниже порога {self.tolerance}")
                break

            parents = self.selection(population, fitness_values)
            self.logs.append(f"Отбор родителей: количество {len(parents)}")

            num_pairs = len(parents) // 2 + len(parents) % 2
            parents_idx = np.random.choice(len(population), size=(num_pairs, 2), replace=True)
            parent_pairs = [(population[i], population[j]) for i, j in parents_idx]
            offspring = [self.crossover(p1, p2) for p1, p2 in parent_pairs]

            offspring = [self.mutate(child) for pair in offspring for child in pair]
            self.logs.append(f"Потомки после мутации: количество {len(offspring)}")

            population = np.vstack((parents, offspring))

        return history

    def selection(self, population, fitness_values):
        indices = np.argsort(fitness_values)
        return population[indices[:len(population) // 2]]

    def crossover(self, parent1, parent2):
        alpha = np.random.rand()
        child1 = alpha * parent1 + (1 - alpha) * parent2
        child2 = alpha * parent2 + (1 - alpha) * parent1
        return child1, child2

    def mutate(self, child):
        mutation_strength = 0.1
        child += np.random.normal(0, mutation_strength, size=child.shape)
        return child

    def get_render(self, func, z_scale, x_axis, y_axis, population_size, generations, **kwargs):
        history = self.run(x_axis, y_axis, population_size, generations, func.calculate)
        genetic_render = GeneticAlgorithmRender()
        genetic_render.z_scale = z_scale
        genetic_render.data = history
        return genetic_render