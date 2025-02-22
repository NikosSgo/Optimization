from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QCheckBox, QVBoxLayout, QHBoxLayout, QComboBox, QGroupBox, QTabWidget
)

#Methods tabs
from src.views.OptimizationMethodTabs.GradientTab import GradientTab
from src.views.OptimizationMethodTabs.GeneticTab import GeneticTab
from src.views.OptimizationMethodTabs.BeeTab import BeeTab
from src.views.OptimizationMethodTabs.BacterialTab import BacterialTab
class OptimizationMethodControls(QWidget):
    def __init__(self,controller = None):
        super().__init__()
        self.controller = controller

        layout = QVBoxLayout()
        # --- Блок "Настройки метода" ---
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        self.gradient_tab = GradientTab()
        self.genetic_tab = GeneticTab()
        self.bee_tab = BeeTab()
        self.bacterial_tab = BacterialTab()
        self.tabs.addTab(self.gradient_tab, "1")
        self.tabs.addTab(self.genetic_tab, "3")
        self.tabs.addTab(self.bee_tab, "5")
        self.tabs.addTab(self.bacterial_tab,"7")

        # Кнопка запуска
        self.run_button = QPushButton("Запустить")
        self.run_button.clicked.connect(self.run_method)
        layout.addWidget(self.run_button)
        self.setLayout(layout)


    def run_method(self):
        if self.controller:
            self.controller.run_method()

