"""
4. Construir un programa que muestre una ventana a través de la cual 
se pueda leer tres datos básicos de 3 mascotas diferentes.

"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel

# Clase Mascota
class Mascota:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad

# Clase de la ventana principal
class MascotaWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle('Ejercicio # 4')
        self.setFixedSize(600, 400)  # Establecer un tamaño fijo para la ventana

        # Crear objetos Mascota
        self.mascotas = [
            Mascota("Fido", "Perro", 5),
            Mascota("Miau", "Gato", 3),
            Mascota("Nemo", "Pez", 1)
        ]

        # Crear y configurar el layout
        layout = QFormLayout()

        # Agregar información de cada mascota al QFormLayout
        for i, mascota in enumerate(self.mascotas):
            # Crear etiquetas para los atributos de cada mascota

            label_titulo = QLabel(f"Lista {i + 1}")
            label_titulo.setStyleSheet("""
                color: Blue;
                font-size: 20px;
                font-family: poppins;
            """)

            label_nombre = QLabel(f"Nombre: {mascota.nombre}")
            label_nombre.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)

            label_tipo = QLabel(f"Tipo: {mascota.tipo}")
            label_tipo.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)

            label_edad = QLabel(f"Edad: {mascota.edad} años")
            label_edad.setStyleSheet("""
                color: green;
                font-size: 16px;
                font-family: poppins;
            """)
            
            # Agregar las etiquetas al layout
            layout.addRow(label_titulo)
            layout.addRow(label_nombre)
            layout.addRow(label_tipo)
            layout.addRow(label_edad)

        # Establecer el layout en la ventana
        self.setLayout(layout)

# Crear la aplicación
app = QApplication(sys.argv)
window = MascotaWindow()
window.show()
sys.exit(app.exec_())

        





        

