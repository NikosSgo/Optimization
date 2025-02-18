from PyQt6.QtWidgets import QMessageBox

class OptimizationFunctionController:
    def __init__(self, view, model=None):
        self._model = model
        self.view = view

    def update_function(self):
        data = self.get_function_data()
        if data:  # Проверяем, что словарь не пустой
            self.model.update_function(data)

    def get_function_data(self) -> dict:
        """Собирает все введённые пользователем данные и возвращает их в виде словаря"""
        try:
            return {
                "function_name": self.view.func_combo.currentText(),
                "x_axis": self._parse_interval(self.view.x_interval_input.text()),
                "y_axis": self._parse_interval(self.view.y_interval_input.text()),
                "z_scale": float(self.view.z_scale_input.text()),
                "display_axes": self.view.axes_checkbox.isChecked(),
                "display_grid": self.view.grid_checkbox.isChecked(),
            }
        except ValueError as e:
            self.show_error_message(f"Ошибка в данных: {e}")
            return {}  # Возвращаем пустой словарь, чтобы модель не обновлялась

    def _parse_interval(self, interval_str: str):
        """Преобразует строку вида '(-5;5)' в кортеж (-5.0, 5.0)"""
        try:
            cleaned = interval_str.replace("(", "").replace(")", "").strip()
            values = cleaned.split(";")
            if len(values) != 2:
                raise ValueError(f"Неверный формат интервала: {interval_str}")
            return float(values[0]), float(values[1])
        except (ValueError, IndexError):
            raise ValueError(f"Ошибка парсинга интервала: {interval_str}")

    def show_error_message(self, message: str):
        """Отображает сообщение об ошибке"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Ошибка")
        msg.setText(message)
        msg.exec()

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model
        self.update_function()
