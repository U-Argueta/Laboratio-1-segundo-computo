"""
3. Construir un programa que muestre una ventana a través de la cual 
   se pueda leer su número de cédula y su nombre completo.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel, QPushButton, QMessageBox

class DUI(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle('Ejercicio # 3')
        self.setFixedSize(600, 250)  # Establecer un tamaño fijo para la ventana

        # Agregar un layout
        form_info = QFormLayout()
        self.setLayout(form_info)

        # Etiquetas para los campos de entrada
        self.dui_label = QLabel("Enter your DUI:", self)
        self.dui_label.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)
        self.username_label = QLabel("Enter your Name:", self)
        self.username_label.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

        # Crear campos de entrada para DUI y nombre
        self.dui_input = QLineEdit(self)
        self.dui_input.setPlaceholderText("00000000-0")
        self.dui_input.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
        """)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter your Name")
        self.username_input.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
        """)

        # Botón para enviar la información
        add_button = QPushButton("Accept", self)
        add_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            padding: 5px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        """)

        add_button.clicked.connect(self.show_info)

        # Etiquetas para mostrar la información
        self.dui_label_infor = QLabel("", self)
        self.dui_label_infor.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

        self.username_label_infor = QLabel("", self)
        self.username_label_infor.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

        # Agregar widgets al layout
        form_info.addRow(self.dui_label, self.dui_input)
        form_info.addRow(self.username_label, self.username_input)
        form_info.addWidget(add_button)
        form_info.addRow(QLabel("", self), self.dui_label_infor)
        form_info.addRow(QLabel("", self), self.username_label_infor)

    def show_info(self):
        dui = self.dui_input.text().strip()
        name = self.username_input.text().strip()

        if not dui or not name:
            QMessageBox.warning(self, "Input Error", "Se deben completar los campos DUI y Nombre.")
            return

        # Actualizar etiquetas con la información ingresada
        self.dui_label_infor.setText(f"DUI: {dui}")
        self.username_label_infor.setText(f"Name: {name}")

# Crear la aplicación
app = QApplication(sys.argv)
login_window = DUI()
login_window.show()
sys.exit(app.exec_())
