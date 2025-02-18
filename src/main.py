import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

#import views
from src.views.OptimizationView import OptimizationView
from src.views.OptimizationMethodControls import OptimizationMethodControls
from src.views.OptimizationMethodResult import OptimizationMethodResult
from src.views.OptimizationFunctionControls import OptimizationFunctionControls
#import controllers
from src.controllers.OptimizationFunctionController import OptimizationFunctionController
from src.controllers.OptimizationMethodController import OptimizationMethodController
#import model
from src.models.OptimizationModel import OptimizationModel


class OptimizationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Optimization methods")
        self.setGeometry(100, 100, 800, 600)
        ##############################################################
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        horizontal_layout = QHBoxLayout(central_widget)
        ##############################################################
        #View
        optimization_view = OptimizationView()
        horizontal_layout.addWidget(optimization_view, stretch=7)

        optimization_method_controls = OptimizationMethodControls()
        optimization_method_result = OptimizationMethodResult()
        optimization_function_controls = OptimizationFunctionControls()

        vertical_widget = QWidget(self)
        vertical_layout = QVBoxLayout(vertical_widget)
        vertical_layout.addWidget(optimization_method_controls)
        vertical_layout.addWidget(optimization_method_result)
        vertical_layout.addWidget(optimization_function_controls)

        horizontal_layout.addWidget(vertical_widget, stretch=3)
        ##############################################################
        #Models
        model = OptimizationModel()
        #Add views as observers to model
        model.add_observer(optimization_view)
        model.add_observer(optimization_method_result)
        ##############################################################
        #Controller
        function_controller = OptimizationFunctionController(optimization_function_controls)
        method_controller = OptimizationMethodController(optimization_method_controls)
        ##############################################################
        #Connect controllers and models
        function_controller.model = model
        method_controller.model = model
        ##############################################################
        #Connect views and controllers
        optimization_function_controls.controller = function_controller
        optimization_method_controls.controller = method_controller

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OptimizationApp()
    window.show()
    sys.exit(app.exec())
