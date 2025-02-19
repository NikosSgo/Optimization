from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QCheckBox, QVBoxLayout, QHBoxLayout, QComboBox, QGroupBox
)

class OptimizationFunctionControls(QWidget):
    def __init__(self,controller = None):
        super().__init__()
        self.controller = controller

        layout = QVBoxLayout()
        # --- Блок "Функция и график" ---
        function_group = QGroupBox("Функция и отображение её графика")
        function_layout = QVBoxLayout()

        functions_list = ["", "Функция Химмельблау","Функция Матьяса","Функция Розенброка"]

        self.func_combo = self._create_labeled_combo(function_layout,"Функция", functions_list)
        self.x_interval_input = self._create_labeled_input(function_layout,"X интервал", "(-5;5)")
        self.y_interval_input = self._create_labeled_input(function_layout,"Y интервал", "(-5;5)")
        self.z_scale_input = self._create_labeled_input(function_layout,"Z масштаб", "1")

        self.func_combo.currentIndexChanged.connect(self._on_data_function_changed)
        self.x_interval_input.editingFinished.connect(self._on_data_function_changed)
        self.y_interval_input.editingFinished.connect(self._on_data_function_changed)
        self.z_scale_input.editingFinished.connect(self._on_data_function_changed)

        # Настройки осей и сетки
        self.axes_checkbox = QCheckBox("Оси")
        self.grid_checkbox = QCheckBox("Сетка")
        self.axes_checkbox.setChecked(True)
        self.grid_checkbox.setChecked(True)
        self.axes_checkbox.stateChanged.connect(self._on_data_function_changed)
        self.grid_checkbox.stateChanged.connect(self._on_data_function_changed)
        function_layout.addWidget(self.axes_checkbox)
        function_layout.addWidget(self.grid_checkbox)
        function_group.setLayout(function_layout)

        layout.addWidget(function_group)
        self.setLayout(layout)

    def _create_labeled_input(self, parent, label_text, default_value=""):
        """ Создаёт горизонтальный layout с меткой и QLineEdit """
        layout = QHBoxLayout()
        label = QLabel(label_text)
        input_field = QLineEdit(default_value)
        layout.addWidget(label)
        layout.addWidget(input_field)
        parent.addLayout(layout)
        return input_field

    def _create_labeled_combo(self, parent, label_text, options):
        """ Создаёт горизонтальный layout с меткой и QComboBox """
        layout = QHBoxLayout()
        label = QLabel(label_text)
        combo_box = QComboBox()
        combo_box.addItems(options)
        layout.addWidget(label)
        layout.addWidget(combo_box)
        parent.addLayout(layout)
        return combo_box

    def _on_data_function_changed(self):
        if self.controller:
            self.controller.update_function()
