"""
6. Utilizar al menos dos rabiobox, combobox y spinbox
"""

import sys
from PyQt5.QtWidgets import QPushButton, QSpinBox, QComboBox, QRadioButton, QHBoxLayout, QMainWindow , QLineEdit ,QApplication, QWidget, QFormLayout, QLabel
from PyQt5.QtCore import Qt

# Informacion del estudiante 
# RabioBox Determinar Genero
# Combobox 1. Beca (Beca 100%, Beca 80% .. etc) 2. Zona (Zona Rural, Zona Urbana)
# Spinbox 1. Edad 2. Grado de estudio

class Estudiante(QWidget):
    def __init__(self):
        super().__init__()
    
    #Configurar la ventana 
        self.setWindowTitle('Ejercicio # 6')
        self.setFixedSize(600, 700) # Establecer un tamaño fijo para la ventana

    # Agregar un layout
        form_students = QFormLayout()
        self.setLayout(form_students)

    # Etiquetas titulo
        self.label_title = QLabel("BECAS UNIVERSITARIAS", self)
        self.label_title.setAlignment(Qt.AlignCenter) 

        self.label_title.setStyleSheet("""
            color: black;
            font-size: 25px;
            font-family: poppins;
            margin-bottom: 20px;
        """)


    # Etiquetas para los campos de entrada
        self.label_code = QLabel("Enter your student code:", self)
        self.label_code.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

        self.label_name = QLabel("Enter your name:", self)
        self.label_name.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

        self.label_lastname = QLabel("Enter your lastname:", self)
        self.label_lastname.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

    # Campos de entrada
        self.input_code = QLineEdit(self)
        self.input_code.setPlaceholderText("##########")
        self.input_code.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
        """)

        self.input_name = QLineEdit(self)
        self.input_name.setPlaceholderText("Enter your name")
        self.input_name.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
        """)

        self.input_lastname = QLineEdit(self)
        self.input_lastname.setPlaceholderText("Enter your lastname")
        self.input_lastname.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
        """)

    # Agregar rabioButton
        self.label_gender = QLabel("Select Gender:", self)
        self.label_gender.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton('Masculino')
        self.male_radio.setStyleSheet("""
            padding:  10, 15, 10, 15;
            font-size: 16px;
            font-family: poppins;
            
        """)
        self.female_radio = QRadioButton('Femenino')
        self.female_radio.setStyleSheet("""
            padding:  10, 15, 10, 15;
            font-size: 16px;
            font-family: poppins;
        """)

        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)

    #Agregar ComboBox 
        self.label_type_scholarship = QLabel("Type of scholarship:", self)
        self.label_type_scholarship.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

        self.scholarship_combo = QComboBox()
        self.scholarship_combo.addItems(['Beca 100%', 'Beca 80%', 'Beca 50%', 'Sin Beca'])
        self.scholarship_combo.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
            
        """)

        self.label_zone = QLabel("Zona:", self)
        self.label_zone.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

        self.zone_combo = QComboBox()
        self.zone_combo.addItems(['Zona Rural', 'Zona Urbana'])
        self.zone_combo.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
            
        """)
    
    #Agregar SpinBox
        self.label_age = QLabel("Enter your age:", self)
        self.label_age.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

        self.age_spinBox = QSpinBox()
        self.age_spinBox.setRange(1, 100)
        self.age_spinBox.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
            
        """)

        self.label_grade = QLabel("Enter your grade:", self)
        self.label_grade.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

        self.grade_spinBox = QSpinBox()
        self.grade_spinBox.setRange(1, 5)
        self.grade_spinBox.setStyleSheet("""
            padding: 5px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
            
        """)

    #Agregar button
         # Botón para enviar la información
        self.add_button = QPushButton("Accept", self)
        self.add_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            padding: 5px;
            margin: 25px, 0, 0,0;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        """)
        self.add_button.clicked.connect(self.show_information)

    #Agregar etiqueta para mostrar la informacion
        self.info_label = QLabel('')
        self.info_label.setStyleSheet("""
            color: green;
            font-size: 16px;
            font-family: poppins;
        """)

    # Agregar los campos al formulario
        form_students.addRow(self.label_title)
        form_students.addRow(self.label_code, self.input_code)
        form_students.addRow(self.label_name, self.input_name)
        form_students.addRow(self.label_lastname, self.input_lastname)
        form_students.addRow(self.label_gender, gender_layout)
        form_students.addRow(self.label_type_scholarship, self.scholarship_combo)
        form_students.addRow(self.label_zone, self.zone_combo)
        form_students.addRow(self.label_age, self.age_spinBox)
        form_students.addRow(self.label_grade, self.grade_spinBox)
        form_students.addRow(self.add_button)
        form_students.addRow(self.info_label)

    def show_information(self):
        name = self.input_name.text()
        lastname = self.input_lastname.text()
        gender = 'Masculino' if self.male_radio.isChecked() else 'Femenino' if self.female_radio.isChecked() else 'No seleccionado'
        scholarship = self.scholarship_combo.currentText()
        zone = self.zone_combo.currentText()
        age = self.age_spinBox.value()
        grade = self.grade_spinBox.value()

        info = (
            f'Nombre: {name}\n'
            f'Apellido: {lastname}\n'
            f'Género: {gender}\n'
            f'Beca: {scholarship}\n'
            f'Zona: {zone}\n'
            f'Edad: {age}\n'
            f'Grado de Estudio: {grade}'
        )

        self.info_label.setText(info)




        
        
    
app = QApplication(sys.argv)
infor_students = Estudiante()
infor_students.show()
sys.exit(app.exec_())