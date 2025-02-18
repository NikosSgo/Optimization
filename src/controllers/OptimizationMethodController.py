from PyQt6.QtWidgets import QMessageBox

class OptimizationMethodController:
    def __init__(self, view, model=None):
        self._model = model
        self.view = view

    def run_method(self):
        data = self.get_method_data()
        if data:
            self.model.run_method(data)

    def get_method_data(self) -> dict:
        """Собирает все введённые пользователем данные и возвращает их в виде словаря"""
        try:
            current_index = self.view.tabs.currentIndex()
            current_widget = self.view.tabs.widget(current_index)
            params = current_widget.get_params()
            if params["method_name"] == "Метод градиентного спуска":
                params["start_x"] = float(params["start_x"])
                params["start_y"] = float(params["start_y"])
                params["step"] = float(params["step"])
                params["count_iterations"] = int(params["count_iterations"])
                params["delay"] = int(float(params["delay"]) * 1000)
            self.model.run_method(params)
        except ValueError as e:
            self.show_error_message(f"Ошибка в данных: {e}")
            return {}

    def show_error_message(self, message: str):
        """Отображает сообщение об ошибке"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Ошибка")
        msg.setText(message)
        msg.exec()
