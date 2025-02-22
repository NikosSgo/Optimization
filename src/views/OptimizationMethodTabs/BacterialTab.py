from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QCheckBox, QVBoxLayout, QHBoxLayout, QComboBox, QGroupBox
)

class BacterialTab(QWidget):
    def __init__(self):
        super().__init__()

        # Основной вертикальный layout
        layout = QVBoxLayout()

        # --- Блок "Настройки метода" ---
        settings_group = QGroupBox("Настройки бактериального алгоритма")
        settings_layout = QVBoxLayout()

        self.population_size = self.create_labeled_input(settings_layout, "Размер популяции", "20")
        self.step_size = self.create_labeled_input(settings_layout, "Шаг хемотаксиса", "0.1")
        self.swim_length = self.create_labeled_input(settings_layout, "Длина плавания", "5")
        self.probability = self.create_labeled_input(settings_layout, "Вероятность", "0.3")
        self.generations = self.create_labeled_input(settings_layout, "Количество поколений", "10")
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
        """ Возвращает параметры алгоритма, считанные из формы """
        return {
            "method_name": "Бактериальный алгоритм",
            "population_size": self.population_size.text(),
            "step_size": self.step_size.text(),
            "swim_length": self.swim_length.text(),
            "probability": self.probability.text(),
            "generations": self.generations.text(),
            "delay": self.delay_input.text(),
        }


