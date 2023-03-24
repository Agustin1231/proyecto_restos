from PySide6.QtWidgets import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property
import random 

class juego(QMainWindow):
    
    def setup(self):
        self.jugador = 1
        # Fondo
        self.set_fixed_size (800,600)
        self.style_sheet = "background: #1A141E"

        
        # Titulo
        self.titulo = QLabel(self)
        self.titulo.geometry = QRect(10,10,780,50)
        self.titulo.text = f"Bienvenido Jugador {self.jugador}"
        self.titulo.alignment = Qt.AlignCenter
        self.titulo.style_sheet = """
            color: white;
            font-size: 25px;
            font-weight: bold;
        """
        # Subtitulo
        self.subtitulo = QLabel(self)
        self.subtitulo.geometry = QRect(10,70,780,50)
        self.subtitulo.text = "Numero De Carta"
        self.subtitulo.alignment = Qt.AlignCenter
        self.subtitulo.style_sheet = """
            color: white;
            font-size: 25px;
            font-weight: bold;
        """

        # Boton
        self.texto_boton = QLabel(self)
        self.texto_boton.geometry = QRect(423.333,121.333,100,50)
        self.texto_boton.text = ""
        self.texto_boton.style_sheet ="""
            background: white;
            font-size: 20px;
        """

        self.boton = QPushButton(self)
        self.boton.text = "Tirar"
        self.boton.geometry = QRect(273.333,121.333,100,50)
        self.boton.alignment = Qt.AlignCenter
        self.boton.clicked.connect(self.tirar_dado)
        self.boton.style_sheet = """
            color: white;
            font-size: 25px;
            font-weight: bold;
            background: #1A191A;
        """

        # Carta
        self.carta_1 = QLabel(self)
        self.carta_1.geometry = QRect(10,190,253.333,195)
        self.carta_1.style_sheet = "background: #3498DB"

        self.carta_2 = QLabel(self)
        self.carta_2.geometry = QRect(273.333,190,253.333,195)
        self.carta_2.style_sheet = "background: #2ECC71"

        self.carta_3 = QLabel(self)
        self.carta_3.geometry = QRect(536.6966,190,253.333,195)
        self.carta_3.style_sheet = "background: #3498DB"

        self.carta_4 = QLabel(self)
        self.carta_4.geometry = QRect(10,395,253.333,195)
        self.carta_4.style_sheet = "background: #2ECC71"

        self.carta_5 = QLabel(self)
        self.carta_5.geometry = QRect(273.333,395,253.333,195)
        self.carta_5.style_sheet = "background: #3498DB"

        self.carta_6 = QLabel(self)
        self.carta_6.geometry = QRect(536.6966,395,253.333,195)
        self.carta_6.style_sheet = "background: #2ECC71"

        
        # Texto carta
        self.texto_carta_1 = QPushButton(self.carta_1)
        self.texto_carta_1.text = "1" 
        self.texto_carta_1.geometry = QRect(107,78,40,40)
        self.texto_carta_1.style_sheet = """
            background: white;
            font-size: 20px;
            color: black;
        """

        self.texto_carta_2 = QPushButton(self.carta_2)
        self.texto_carta_2.text = "2" 
        self.texto_carta_2.geometry = QRect(107,78,40,40)
        self.texto_carta_2.style_sheet = """
            background: white;
            font-size: 20px;
            color: black;
        """

        self.texto_carta_3 = QPushButton(self.carta_3)
        self.texto_carta_3.text = "3" 
        self.texto_carta_3.geometry = QRect(107,78,40,40)
        self.texto_carta_3.style_sheet = """
            background: white;
            font-size: 20px;
            color: black;
        """

        self.texto_carta_4 = QPushButton(self.carta_4)
        self.texto_carta_4.text = "4" 
        self.texto_carta_4.geometry = QRect(107,78,40,40)
        self.texto_carta_4.style_sheet = """
            background: white;
            font-size: 20px;
            color: black;
        """

        self.texto_carta_5 = QPushButton(self.carta_5)
        self.texto_carta_5.text = "5" 
        self.texto_carta_5.geometry = QRect(107,78,40,40)
        self.texto_carta_5.style_sheet = """
            background: white;
            font-size: 20px;
            color: black;
        """

        self.texto_carta_6 = QPushButton(self.carta_6)
        self.texto_carta_6.text = "6" 
        self.texto_carta_6.geometry = QRect(107,78,40,40)
        self.texto_carta_6.style_sheet = """
            background: white;
            font-size: 20px;
            color: black;
        """

        # Plantilla reto
        self.dialogo = QDialog(self)
        self.dialogo.set_fixed_size (500,400)
        self.dialogo.style_sheet = "background: #1A141E"
        
        # Titulo dialogo
        self.dialogo_titulo = QLabel(self.dialogo)
        self.dialogo_titulo.geometry = QRect(10,10,480,50)
        self.dialogo_titulo.text = "Reto"
        self.dialogo_titulo.alignment = Qt.AlignCenter
        self.dialogo_titulo.style_sheet = """
            color: white;
            font-size: 25px;
            font-weight: bold;
        """

        # contenedor reto
        self.dialogo_fr_reto = QFrame(self.dialogo)
        self.dialogo_fr_reto.geometry = QRect(10,70,480,260)        
        self.dialogo_fr_reto.style_sheet = "background: red;"

        # Descripccion reto
        self.texto_reto = QLabel(self.dialogo_fr_reto)
        self.texto_reto.text = ""
        self.texto_reto.geometry = QRect(5,0,480,60)
        self.texto_reto.style_sheet = """
            color: white;
            font-size: 20px;
        """

        # Salidas programa
        self.salidas = QLabel(self.dialogo_fr_reto)
        self.salidas.geometry = QRect(5,60,480,180)
        self.salidas.text = "                Salidas             "
        self.salidas.style_sheet = """
            color: white;
            font-size: 20px;
        """        

        # Siguiente jugador
        self.siguiente_jugador = QPushButton(self.dialogo)
        self.siguiente_jugador.text = "Siguiente Jugador"
        self.siguiente_jugador.geometry = QRect(320,340,170,50)
        self.siguiente_jugador.clicked.connect(self.dialogo.close) # Cerrar el dialogo
        self.siguiente_jugador.clicked.connect(self.cambio_jugador)
        self.siguiente_jugador.style_sheet = """
            background: red;
            color: white;
            font-size: 20px
        """
        
    def tirar_dado(self):
        n_carta = random.randint(1,6)
        self.texto_boton.text = f"        {n_carta}" # Los espacios son para que este centrado el texto

        if n_carta == 1:
            self.texto_carta_1.style_sheet = """
                color: red;
                background: white;
                font-size: 20px;
            """
            self.carta_1.style_sheet = "background: red;"
            self.texto_carta_1.clicked.connect(self.reto)
        
        elif n_carta == 2:
            self.texto_carta_2.style_sheet = """
                color: red;
                background: white;
                font-size: 20px;
            """
            self.carta_2.style_sheet = "background: red;"
            self.texto_carta_2.clicked.connect(self.reto)
        
        elif n_carta == 3:
            self.texto_carta_3.style_sheet = """
                color: red;
                background: white;
                font-size: 20px;
            """
            self.carta_3.style_sheet = "background: red;"
            self.texto_carta_3.clicked.connect(self.reto)
        
        elif n_carta == 4:
            self.texto_carta_4.style_sheet = """
                color: red;
                background: white;
                font-size: 20px;
            """
            self.carta_4.style_sheet = "background: red;"
            self.texto_carta_4.clicked.connect(self.reto)
        
        elif n_carta == 5:
            self.texto_carta_5.style_sheet = """
                color: red;
                background: white;
                font-size: 20px;
            """
            self.carta_5.style_sheet = "background: red;"
            self.texto_carta_5.clicked.connect(self.reto)

        elif n_carta == 6:
            self.texto_carta_6.style_sheet = """
                color: red;
                background: white;
                font-size: 20px;
            """
            self.carta_6.style_sheet = "background: red;"
            self.texto_carta_6.clicked.connect(self.reto)

    def reto(self):
        if self.texto_boton.text == "        1":
            # contenedor reto
            self.dialogo_fr_reto = QFrame(self.dialogo)
            self.dialogo_fr_reto.geometry = QRect(10,70,480,260)        
            self.dialogo_fr_reto.style_sheet = "background: #3498DB;"

            # Descripccion reto
            self.texto_reto = QLabel(self.dialogo_fr_reto)
            self.texto_reto.text = "Diseñe un programa en 10 min donde se obtengan \ndos numero aleatorios en un rango de 0 a 100"
            self.texto_reto.geometry = QRect(5,0,480,60)
            self.texto_reto.style_sheet = """
                color: white;
                font-size: 20px;
            """

            # Salidas programa
            self.salidas = QLabel(self.dialogo_fr_reto)
            self.salidas.geometry = QRect(5,60,480,180)
            self.salidas.text = "                Salidas             \n* Suma\n* Multiplicacion\n* Resta numero mayor-menor"
            self.salidas.style_sheet = """
                color: white;
                font-size: 20px;
            """        
            self.dialogo.show()

            self.texto_carta_1.style_sheet = """
                color: black;
                background: white;
                font-size: 20px;
            """
            self.carta_1.style_sheet = "background: #3498DB;"
            self.texto_boton.text =""
        
        elif self.texto_boton.text == "        2":
            
            # contenedor reto
            self.dialogo_fr_reto = QFrame(self.dialogo)
            self.dialogo_fr_reto.geometry = QRect(10,70,480,260)        
            self.dialogo_fr_reto.style_sheet = "background: #2ECC71;"

            # Descripccion reto
            self.texto_reto = QLabel(self.dialogo_fr_reto)
            self.texto_reto.text = "Diseñe un programa en 10 min donde se escribira un \ntexto y se contara el numero de vocales"
            self.texto_reto.geometry = QRect(5,0,480,60)
            self.texto_reto.style_sheet = """
                color: white;
                font-size: 20px;
            """

            # Salidas programa
            self.salidas = QLabel(self.dialogo_fr_reto)
            self.salidas.geometry = QRect(5,60,480,180)
            self.salidas.text = "                Salidas             \n* Cuales vocales salen\n* Numero de vocales en el texto\n* Que vocal sale mas"
            self.salidas.style_sheet = """
                color: white;
                font-size: 20px;
            """
            self.dialogo.show()
            self.texto_carta_2.style_sheet = """
                color: black;
                background: white;
                font-size: 20px;
            """
            self.carta_2.style_sheet = "background: #2ECC71;"
            self.texto_boton.text =""
        
        elif self.texto_boton.text == "        3":
                
            # contenedor reto
            self.dialogo_fr_reto = QFrame(self.dialogo)
            self.dialogo_fr_reto.geometry = QRect(10,70,480,260)        
            self.dialogo_fr_reto.style_sheet = "background: #3498DB;"

            # Descripccion reto
            self.texto_reto = QLabel(self.dialogo_fr_reto)
            self.texto_reto.text = "Escribir un programa en 10 min que lea un entero \npositivo y calcule la suma de los numeros hasta el \ningresado, con la siguiente formula suma = (n(n+1))"
            self.texto_reto.geometry = QRect(5,0,480,80)
            self.texto_reto.style_sheet = """
                color: white;
                font-size: 20px;
            """

            # Salidas programa
            self.salidas = QLabel(self.dialogo_fr_reto)
            self.salidas.geometry = QRect(5,100,480,160)
            self.salidas.text = "                Salidas             \n* Mostrar si es mayor de edad\n* Mostrar si es menor de edad\n* Mensaje con su nombre y edad"
            self.salidas.style_sheet = """
                color: white;
                font-size: 20px;
            """        
            self.dialogo.show()
            self.texto_carta_3.style_sheet = """
                color: black;
                background: white;
                font-size: 20px;
            """
            self.carta_3.style_sheet = "background: #3498DB;"
            self.texto_boton.text =""
        
        elif self.texto_boton.text == "        4":
            
            # contenedor reto
            self.dialogo_fr_reto = QFrame(self.dialogo)
            self.dialogo_fr_reto.geometry = QRect(10,70,480,260)        
            self.dialogo_fr_reto.style_sheet = "background: #2ECC71;"

            # Descripccion reto
            self.texto_reto = QLabel(self.dialogo_fr_reto)
            self.texto_reto.text = "Diseñe un programa en 10 min donde se recibira\nla altura , los lados de un triangulo equilatero "
            self.texto_reto.geometry = QRect(5,0,480,60)
            self.texto_reto.style_sheet = """
                color: white;
                font-size: 20px;
            """

            # Salidas programa
            self.salidas = QLabel(self.dialogo_fr_reto)
            self.salidas.geometry = QRect(5,60,480,180)
            self.salidas.text = "                Salidas             \n* Area del triangulo\n* Perimetro del triangulo\n* Altura del triangulo"
            self.salidas.style_sheet = """
                color: white;
                font-size: 20px;
            """        
            self.dialogo.show()
            
            self.texto_carta_4.style_sheet = """
                color: black;
                background: white;
                font-size: 20px;
            """
            self.carta_4.style_sheet = "background: #2ECC71;"
            self.texto_boton.text =""
        
        elif self.texto_boton.text == "        5":
            
            # contenedor reto
            self.dialogo_fr_reto = QFrame(self.dialogo)
            self.dialogo_fr_reto.geometry = QRect(10,70,480,260)        
            self.dialogo_fr_reto.style_sheet = "background: #3498DB;"

            # Descripccion reto
            self.texto_reto = QLabel(self.dialogo_fr_reto)
            self.texto_reto.text = "Diseñar un programa en 6 min donde se introduzca\nun nombre y se cuente el numero de letras que tiene"
            self.texto_reto.geometry = QRect(5,0,480,80)
            self.texto_reto.style_sheet = """
                color: white;
                font-size: 20px;
            """

            # Salidas programa
            self.salidas = QLabel(self.dialogo_fr_reto)
            self.salidas.geometry = QRect(5,100,480,160)
            self.salidas.text = "                Salidas             \n* Mostrar el nombre en mayusuculas\n* Mostrar el numero de letras\n"
            self.salidas.style_sheet = """
                color: white;
                font-size: 20px;
            """        
            self.dialogo.show()
            self.texto_carta_5.style_sheet = """
                color: black;
                background: white;
                font-size: 20px;
            """
            self.carta_5.style_sheet = "background: #3498DB;"
            self.texto_boton.text =""
        
        elif self.texto_boton.text == "        6":
            
            # contenedor reto
            self.dialogo_fr_reto = QFrame(self.dialogo)
            self.dialogo_fr_reto.geometry = QRect(10,70,480,260)        
            self.dialogo_fr_reto.style_sheet = "background: #2ECC71;"

            # Descripccion reto
            self.texto_reto = QLabel(self.dialogo_fr_reto)
            self.texto_reto.text = "Diseñe un programa en 5 min donde se recibira\n el nombre y la edad."
            self.texto_reto.geometry = QRect(5,0,480,60)
            self.texto_reto.style_sheet = """
                color: white;
                font-size: 20px;
            """

            # Salidas programa
            self.salidas = QLabel(self.dialogo_fr_reto)
            self.salidas.geometry = QRect(5,60,480,180)
            self.salidas.text = "                Salidas             \n* Mostrar si es mayor de edad\n* Mostrar si es menor de edad\n* Mensaje con su nombre y edad"
            self.salidas.style_sheet = """
                color: white;
                font-size: 20px;
            """
            self.dialogo.show()
            
            self.texto_carta_6.style_sheet = """
                color: black;
                background: white;
                font-size: 20px;
            """
            self.carta_6.style_sheet = "background: #2ECC71;"
            self.texto_boton.text =""

    def cambio_jugador(self):
        self.jugador += 1
        self.titulo.text = f"Bienvenido Jugador {self.jugador}"

import sys

app = QApplication(sys.argv)
window = juego()
window.setup()
window.show()
sys.exit(app.exec())   