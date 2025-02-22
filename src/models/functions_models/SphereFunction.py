from src.models.functions_models.OptimizationFunction import OptimizationFunction

class SphereFunction(OptimizationFunction):
    def calculate(self,x,y):
        return 1 / (1 + x ** 2 + y ** 2)