"""
2. Construir un programa que muestre una ventana y que lea una clave
   secreta sin mostrar los caracteres que la componen.  

"""

import sys 
from PyQt5.QtCore import Qt
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

# Agregar lista de usario con claves

users = [
    ("Carlos", "carlos"),
    ("Ulices", "Ulices")
]

class Login(qtw.QWidget):
    def __init__(self):
        super().__init__()

     # Configurar la ventana de inicio de sesión
        self.setWindowTitle('Ejercicio # 2')
        self.setFixedSize(300, 150)  # Establecer un tamaño fijo para la ventana

     # Agregar un layout
        form_login = qtw.QFormLayout()
        self.setLayout(form_login)

    # Etiquetas para los campos de entrada
        self.username_label = qtw.QLabel("Username:", self)
        self.username_label.setStyleSheet("""
            color:green;
            font-size: 16px;
            font-family: poppins;

        """)
        self.password_label =  qtw.QLabel("Password:", self)
        self.password_label.setStyleSheet("""
            color:green;
            font-size: 16px;
            font-family: poppins;
        """)

     # Crear campos de entrada para nombre de usuario y contraseña
        self.username_input = qtw.QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
        """)

        self.password_input = qtw.QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
        """)
        self.password_input.setEchoMode(qtw.QLineEdit.Password)  # Ocultar caracteres
    
    # Botón para enviar las credenciales
        login_button = qtw.QPushButton("Login", self)
        login_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            padding: 5px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        """)

        login_button.clicked.connect(self.login)

 # Agregar widgets al layout
        form_login.addRow(self.username_label, self.username_input)
        form_login.addRow(self.password_label, self.password_input)
        form_login.addWidget(login_button)

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        # Validar las credenciales
        if (username, password) in users:
            qtw.QMessageBox.information(self, "Welcome", f' Hello, {username}')
        else:
            qtw.QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")

# Crear la aplicación
app = qtw.QApplication(sys.argv)
login_window = Login()
login_window.show()
sys.exit(app.exec_())
