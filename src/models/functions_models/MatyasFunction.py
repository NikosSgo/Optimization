from src.models.functions_models.OptimizationFunction import OptimizationFunction

class MatyasFunction(OptimizationFunction):
    def calculate(self,x,y):
        return 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y