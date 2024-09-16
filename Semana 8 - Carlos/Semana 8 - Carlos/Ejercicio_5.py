"""
5. Construir un programa que muestre una ventana a través de la cual 
   se puedan leer 10 datos característicos de una persona.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel

# Clase Persona
class Persona:
    def __init__(self, dui, nombre, apellido, edad, direccion, correo, telefono, genero, profesion, estado_famaliar  ):
        self.dui = dui
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.correo = correo
        self.telefono = telefono
        self.genero = genero
        self.profesion = profesion
        self.estado_familiar = estado_famaliar

# Clase de la ventana principal
class PersonaWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle('Ejercio # 5')
        self.setFixedSize(600, 400)  # Establecer un tamaño fijo para la ventana

        # Crear objetos Mascota
        self.personas = [
            Persona("00000000-0", "Juan Calor", "Ramirez Vesquez", 58, "Santa Ana, El Salvador", "juan540@gmail.com", "+000 000-000", "Masculino", "Ing. Sistema", "Casado")
            
        ]

        # Crear y configurar el layout
        layout = QFormLayout()

        # Agregar información de cada mascota al QFormLayout
        for i, persona in enumerate(self.personas):
            # Crear etiquetas para los atributos de cada mascota

            label_titulo = QLabel(f"Informacion Personal")
            label_titulo.setStyleSheet("""
                color: Blue;
                font-size: 20px;
                font-family: poppins;
            """)

            label_dui = QLabel(f"Numero de DUI: {persona.dui}")
            label_dui.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)

            label_nombre = QLabel(f"Nombre: {persona.nombre}")
            label_nombre.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)

            label_apellido= QLabel(f"Apellido: {persona.apellido}")
            label_apellido.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)

            label_edad = QLabel(f"Edad: {persona.edad}")
            label_edad.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)

            label_direccion = QLabel(f"Direccion: {persona.direccion}")
            label_direccion.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)


            labal_correo = QLabel(f"Correo: {persona.correo}")
            labal_correo.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)


            label_telefono = QLabel(f"telefono : {persona.telefono}")
            label_telefono.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)


            label_genero = QLabel(f"Genero: {persona.genero}")
            label_genero.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)

            label_profesion = QLabel(f"Profesion: {persona.profesion}")
            label_profesion.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)

            label_estado_famaliar = QLabel(f"Estado Familiar: {persona.estado_familiar}")
            label_estado_famaliar.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)

            # Agregar las etiquetas al layout
            layout.addRow(label_titulo)
            layout.addRow(label_dui)
            layout.addRow(label_nombre)
            layout.addRow(label_apellido)
            layout.addRow(label_edad)
            layout.addRow(label_direccion)
            layout.addRow(labal_correo)
            layout.addRow(label_telefono)
            layout.addRow(label_genero)
            layout.addRow(label_profesion)
            layout.addRow(label_estado_famaliar)

        # Establecer el layout en la ventana
        self.setLayout(layout)

# Crear la aplicación
app = QApplication(sys.argv)
window = PersonaWindow()
window.show()
sys.exit(app.exec_())

        





        

