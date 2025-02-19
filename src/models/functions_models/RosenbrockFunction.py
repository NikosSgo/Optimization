from src.models.functions_models.OptimizationFunction import OptimizationFunction

class RosenbrockFunction(OptimizationFunction):
    def calculate(self,x,y):
        return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
