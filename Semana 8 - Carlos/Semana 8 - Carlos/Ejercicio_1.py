"""
Construir un programa que muestre una ventana en la cual aparezca su nombre completo y su edad centrados.

"""

import sys
from PyQt5.QtCore import Qt
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # Configurar la ventana principal
        self.setWindowTitle('Ejercicio #1')
        self.setFixedSize(600, 300)  # Establecer un tamaño fijo para la ventana
        
        # Agregar un layout
        form_main = qtw.QFormLayout()
        self.setLayout(form_main)

        # Agregar input
        input_name = qtw.QLineEdit(self)
        input_age = qtw.QLineEdit(self)

        # Agregar los labels
        lb_name = qtw.QLabel("")
        lb_name.setFont(qtg.QFont("poppins", 18))  # Cambiar fuente
        lb_name.setStyleSheet("color: #333;")  # Cambiar color del texto
        lb_name.setAlignment(Qt.AlignCenter) 

        lb_age = qtw.QLabel("")
        lb_age.setFont(qtg.QFont("poppins", 18))  # Cambiar fuente
        lb_age.setStyleSheet("color: #333;")  # Cambiar color del texto
        lb_age.setAlignment(Qt.AlignCenter) 

        # Estilos para los inputs
        input_name.setPlaceholderText("Enter your name")
        input_name.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
        """)
        
        input_age.setPlaceholderText("Enter your age")
        input_age.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
        """)

        # Estilos para el botón
        add_button = qtw.QPushButton("Add")
        add_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            padding: 5px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        """)

        # Agregar filas al layout
        form_main.addRow("Enter your name: ", input_name)
        form_main.addRow("Enter your age: ", input_age)
        form_main.addRow(add_button)
        form_main.addRow(lb_name)
        form_main.addRow(lb_age)

        # Definir función para el botón
        def btnAgregar():
            lb_name.setText(f'Name: {input_name.text()}')
            lb_age.setText(f'Age: {input_age.text()} year old')
        
        # Conectar el clic del botón a la función
        add_button.clicked.connect(btnAgregar)

# Crear la aplicación
app = qtw.QApplication(sys.argv)
User_Info = MainWindow()
User_Info.show()
sys.exit(app.exec_())
