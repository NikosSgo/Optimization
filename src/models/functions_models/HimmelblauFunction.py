from src.models.functions_models.OptimizationFunction import OptimizationFunction

class HimmelblauFunction(OptimizationFunction):
    def calculate(self,x,y):
        return (x**2+y-11)**2 + (x+y**2-7)**2