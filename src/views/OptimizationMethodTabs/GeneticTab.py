from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QCheckBox, QVBoxLayout, QHBoxLayout, QComboBox, QGroupBox
)

class GeneticTab(QWidget):
    def __init__(self,controller = None):
        super().__init__()
        layout = QVBoxLayout()
        # --- Блок "Настройки метода" ---
        settings_group = QGroupBox("Настройки генетического алгоритма")
        settings_layout = QVBoxLayout()

        self.population_size = self.create_labeled_input(settings_layout,"Размер популяции", "20")
        self.generations = self.create_labeled_input(settings_layout,"Количество поколений", "10")

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

    def get_params(self):
        return {
            "method_name": "Генетический алгоритм",
            "population_size": self.population_size.text(),
            "generations": self.generations.text(),
            "delay": self.delay_input.text(),
        }


