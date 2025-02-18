from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QCheckBox, QVBoxLayout, QHBoxLayout, QComboBox, QGroupBox
)

class GradientTab(QWidget):
    def __init__(self,controller = None):
        super().__init__()
        layout = QVBoxLayout()
        # --- Блок "Настройки метода" ---
        settings_group = QGroupBox("Настройки градиентного спуска")
        settings_layout = QVBoxLayout()

        self.x_input = self.create_labeled_input(settings_layout,"X", "-1")
        self.y_input = self.create_labeled_input(settings_layout,"Y", "-1")

        self.step_input = self.create_labeled_input(settings_layout,"Начальный шаг", "0.5")
        self.iterations_input = self.create_labeled_input(settings_layout,"Число итераций", "100")
        self.delay_input = self.create_labeled_input(settings_layout, "Задержка", "0.5")

        settings_group.setLayout(settings_layout)

        layout.addWidget(settings_group)

        self.setLayout(layout)

    def create_labeled_input(self, parent, label_text, default_value=""):
        """ Создаёт горизонтальный layout с меткой и QLineEdit """
        layout = QHBoxLayout()
        label = QLabel(label_text)
        input_field = QLineEdit(default_value)
        layout.addWidget(label)
        layout.addWidget(input_field)
        parent.addLayout(layout)
        return input_field

    def create_labeled_combo(self, parent, label_text, options):
        """ Создаёт горизонтальный layout с меткой и QComboBox """
        layout = QHBoxLayout()
        label = QLabel(label_text)
        combo_box = QComboBox()
        combo_box.addItems(options)
        layout.addWidget(label)
        layout.addWidget(combo_box)
        parent.addLayout(layout)
        return combo_box

    def get_params(self):
        return {
            "method_name": "Метод градиентного спуска",
            "start_x": self.x_input.text(),
            "start_y": self.y_input.text(),
            "step": self.step_input.text(),
            "count_iterations": self.iterations_input.text(),
            "delay": self.delay_input.text(),
        }


