from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QCheckBox, QVBoxLayout, QHBoxLayout, QComboBox, QGroupBox
)

class OptimizationMethodResult(QWidget):
    def __init__(self,controller = None):
        super().__init__()
        self.controller = controller
        # --- Блок "Результаты" ---
        layout = QVBoxLayout()

        result_group = QGroupBox("Выполнение и результаты")
        result_layout = QVBoxLayout()
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        result_layout.addWidget(self.result_text)
        result_group.setLayout(result_layout)

        layout.addWidget(result_group)
        self.setLayout(layout)

    #Вызывается из model
    def update_state(self,data):
        if "optimization_method_result" in data:
            logs = data["optimization_method_result"]["run_method"]
            logs = "\n".join(logs)
            self.result_text.clear()
            self.result_text.append(logs)
            self.update()


