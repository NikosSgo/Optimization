from src.views.functions_render.OptimizationFunctonRender import OptimizationFunctionRender
#import functions models
from src.models.functions_models.MatyasFunction import MatyasFunction
from src.models.functions_models.HimmelblauFunction import HimmelblauFunction
#import methods models
from src.models.methods_models.GradientDescent import GradientDescent

class OptimizationModel:
    def __init__(self):
        self.current_function = ""
        self.functions = {
            "Функция Химмельблау": HimmelblauFunction(),
            "Функция Матьяса": MatyasFunction(),

        }

        self.methods = {
            "Метод градиентного спуска": GradientDescent(),
        }

        self._x_axis = (-5,5)
        self._y_axis = (-5,5)
        self._z_scale = 1
        self.display_axes = True
        self.display_grid = True

        self.observers = []

    def add_observer(self,observer):
        self.observers.append(observer)

    def notify(self,data):
        for observer in self.observers:
            observer.update_state(data)

    def to_dict(self):
        return {
            "function_name": self.current_function,
            "x_axis": self._x_axis,
            "y_axis": self._y_axis,
            "display_axes": self.display_axes,
            "display_grid": self.display_grid,
        }

    def update_function(self, params):
        self.x_axis = params["x_axis"]
        self.y_axis = params["y_axis"]
        self.z_scale = params["z_scale"]
        self.display_grid = params["display_grid"]
        self.display_axes = params["display_axes"]

        self.current_function = params["function_name"]

        if self.current_function:
            function_render = self.functions[self.current_function].get_render(self.x_axis,self.y_axis, self.z_scale)
            func_update_data = {
                "optimization_view": {
                    "update_function" : self.to_dict() | {"func": function_render
                    }
            }}
            self.notify(func_update_data)
        else:
            empty_func_update_data = {
                "optimization_view": {
                    "update_function": self.to_dict() | {"func": OptimizationFunctionRender()
                    }
            }}
            self.notify(empty_func_update_data)

    def axis_validation(self,value):
        return (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(x, float) for x in value))

    def run_method(self, params):

        current_method = params["method_name"]
        method = self.methods[current_method]

        if self.current_function:
            func = self.functions[self.current_function]
            method_render = method.get_render(func,self.z_scale,**params)
            method_run_data = {
                "optimization_view": {
                    "run_method": {
                        "delay": params["delay"],
                        "method": method_render
                    }
                },
                "optimization_method_result": {
                    "run_method": method.logs
                }
            }
            self.notify(method_run_data)


    @property
    def x_axis(self):
        return self._x_axis

    @x_axis.setter
    def x_axis(self, value):
        if self.axis_validation(value):
            self._x_axis = value

    @property
    def y_axis(self):
        return self._y_axis

    @y_axis.setter
    def y_axis(self, value):
        if self.axis_validation(value):
            self._y_axis = value

    @property
    def z_scale(self):
        return self._z_scale

    @z_scale.setter
    def z_scale(self,z_scale):
        if isinstance(z_scale,float):
            self._z_scale = z_scale

