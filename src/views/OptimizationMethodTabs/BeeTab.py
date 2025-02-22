from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QCheckBox, QVBoxLayout, QHBoxLayout, QComboBox, QGroupBox
)

class BeeTab(QWidget):
    def __init__(self):
        super().__init__()

        # Основной вертикальный layout
        layout = QVBoxLayout()

        # --- Блок "Настройки метода" ---
        settings_group = QGroupBox("Настройки пчелиного алгоритма")
        settings_layout = QVBoxLayout()

        self.scout_bees = self.create_labeled_input(settings_layout, "Количество пчёл разведчиков", "20")
        self.selected_bees = self.create_labeled_input(settings_layout, "Количество выбранных пчёл", "5")
        self.elite_bees = self.create_labeled_input(settings_layout, "Количество элитных пчёл", "3")
        self.generations = self.create_labeled_input(settings_layout, "Количество поколений", "10")
        self.neighborhood_size = self.create_labeled_input(settings_layout, "Размер окрестности", "0.1")
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
            "method_name": "Пчелиный алгоритм",
            "scout_bees": self.scout_bees.text(),
            "selected_bees": self.selected_bees.text(),
            "elite_bees": self.elite_bees.text(),
            "generations": self.generations.text(),
            "neighborhood_size": self.neighborhood_size.text(),
            "delay": self.delay_input.text(),
        }


