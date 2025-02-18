from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QCheckBox, QVBoxLayout, QHBoxLayout, QComboBox, QGroupBox, QTabWidget
)

#Methods tabs
from src.views.OptimizationMethodTabs.GradientTab import GradientTab

class OptimizationMethodControls(QWidget):
    def __init__(self,controller = None):
        super().__init__()
        self.controller = controller

        layout = QVBoxLayout()
        # --- Блок "Настройки метода" ---
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        self.gradient_tab = GradientTab()
        self.tabs.addTab(self.gradient_tab, "1")

        # Кнопка запуска
        self.run_button = QPushButton("Запустить")
        self.run_button.clicked.connect(self.run_method)
        layout.addWidget(self.run_button)
        self.setLayout(layout)


    def run_method(self):
        if self.controller:
            self.controller.run_method()

