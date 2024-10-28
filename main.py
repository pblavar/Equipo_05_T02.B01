from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon  # Importa QIcon para manejar íconos
from login import Ui_MainWindow as LoginWindow
from registro import Ui_MainWindow as RegistroWindow
from ventanas import obtener_posicion, colocar_ventana 
import sys
import ctypes

# Establecer el identificador único de la aplicación
myappid = 'proyectoInterfaces.Equipo05'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        # Crear las ventanas
        self.login_window = QMainWindow()
        self.registro_window = QMainWindow()
        
        # Instanciar las interfaces gráficas generadas por Qt Designer
        self.ui_login = LoginWindow()
        self.ui_registro = RegistroWindow()

        # Configurar las interfaces en las ventanas
        self.ui_login.setupUi(self.login_window)
        self.ui_registro.setupUi(self.registro_window)

        # Cargar y establecer íconos para las ventanas
        self.login_window.setWindowIcon(QIcon("img/library64.ico"))
        self.registro_window.setWindowIcon(QIcon("img/library64.ico"))

        # Establecer títulos para las ventanas
        self.login_window.setWindowTitle(" Login - La Estantería de Don Librote")  # Título para la ventana de login
        self.registro_window.setWindowTitle(" Registro - La Estantería de Don Librote")  # Título para la ventana de registro

        # Conectar botones a las funciones correspondientes
        self.ui_login.button_register.clicked.connect(self.show_registro)  # Botón "Registrarse"
        self.ui_registro.button_volver.clicked.connect(self.show_login)  # Botón "Volver"

        # Mostrar la ventana de login al iniciar
        self.login_window.show()

    # Función para mostrar la ventana de registro
    def show_registro(self):
        # Obtener la posición de la ventana actual
        obtener_posicion(self.login_window)
        self.login_window.hide()  # Ocultar ventana de login

        # Colocar la ventana de registro en la misma posición
        colocar_ventana(self.registro_window)
        self.registro_window.show()  # Mostrar ventana de registro

    # Función para volver a la ventana de login
    def show_login(self):
        # Obtener la posición de la ventana actual
        obtener_posicion(self.registro_window)
        self.registro_window.hide()  # Ocultar ventana de registro

        # Colocar la ventana de login en la misma posición
        colocar_ventana(self.login_window)
        self.login_window.show()  # Mostrar ventana de login

    # Ejecutar la aplicación
    def run(self):
        sys.exit(self.app.exec())

# Código principal
if __name__ == "__main__":
    controller = MainController()
    controller.run()
