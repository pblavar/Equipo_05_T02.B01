# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
    
import img.fondoLogin_rc
import img.logoLogin_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setMaximumSize(QSize(800, 500))
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"")
        self.action_limpiar_celdas = QAction(MainWindow)
        self.action_limpiar_celdas.setObjectName(u"action_limpiar_celdas")
        self.action_acerca_de = QAction(MainWindow)
        self.action_acerca_de.setObjectName(u"action_acerca_de")
        self.action_espannol = QAction(MainWindow)
        self.action_espannol.setObjectName(u"action_espannol")
        self.action_ingles = QAction(MainWindow)
        self.action_ingles.setObjectName(u"action_ingles")
        self.action_cerrar = QAction(MainWindow)
        self.action_cerrar.setObjectName(u"action_cerrar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_inicio = QPushButton(self.centralwidget)
        self.button_inicio.setObjectName(u"button_inicio")
        self.button_inicio.setGeometry(QRect(60, 370, 131, 31))
        self.button_inicio.setStyleSheet(u"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(85, 170, 255, 255));\n"
"font: 700 12pt \"Tahoma\";\n"
"color: white;")
        self.label_nombre_usuario = QLabel(self.centralwidget)
        self.label_nombre_usuario.setObjectName(u"label_nombre_usuario")
        self.label_nombre_usuario.setGeometry(QRect(60, 170, 151, 16))
        self.label_nombre_usuario.setStyleSheet(u"font: 700 10pt \"Tahoma\";\n"
"color: rgb(0, 0, 0);")
        self.line_edit_usuario = QLineEdit(self.centralwidget)
        self.line_edit_usuario.setObjectName(u"line_edit_usuario")
        self.line_edit_usuario.setGeometry(QRect(60, 200, 411, 22))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setKerning(True)
        self.line_edit_usuario.setFont(font)
        self.line_edit_usuario.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"	\n"
"	background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: gray;\n"
"}")
        self.line_edit_contrasenna = QLineEdit(self.centralwidget)
        self.line_edit_contrasenna.setObjectName(u"line_edit_contrasenna")
        self.line_edit_contrasenna.setGeometry(QRect(60, 300, 411, 22))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        self.line_edit_contrasenna.setFont(font1)
        self.line_edit_contrasenna.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(247, 247, 247);\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: gray;\n"
"}")
        self.line_edit_contrasenna.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_titulo = QLabel(self.centralwidget)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(125, 22, 361, 51))
        self.label_titulo.setStyleSheet(u"font: 700 18pt \"Tahoma\";\n"
"color: rgb(0, 0, 0);")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_contrasenna = QLabel(self.centralwidget)
        self.label_contrasenna.setObjectName(u"label_contrasenna")
        self.label_contrasenna.setGeometry(QRect(60, 270, 91, 16))
        self.label_contrasenna.setStyleSheet(u"font: 700 10pt \"Tahoma\";\n"
"color: rgb(0, 0, 0);")
        self.label_subtitulo = QLabel(self.centralwidget)
        self.label_subtitulo.setObjectName(u"label_subtitulo")
        self.label_subtitulo.setGeometry(QRect(60, 100, 231, 41))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_subtitulo.setFont(font2)
        self.label_subtitulo.setStyleSheet(u"font: 700 16pt \"Tahoma\";\n"
"color: rgb(0, 0, 0);")
        self.line_contrasenna = QFrame(self.centralwidget)
        self.line_contrasenna.setObjectName(u"line_contrasenna")
        self.line_contrasenna.setGeometry(QRect(60, 320, 411, 10))
        self.line_contrasenna.setFrameShape(QFrame.Shape.HLine)
        self.line_contrasenna.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_usuario = QFrame(self.centralwidget)
        self.line_usuario.setObjectName(u"line_usuario")
        self.line_usuario.setGeometry(QRect(60, 220, 411, 10))
        self.line_usuario.setFrameShape(QFrame.Shape.HLine)
        self.line_usuario.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_imagen = QLabel(self.centralwidget)
        self.label_imagen.setObjectName(u"label_imagen")
        self.label_imagen.setGeometry(QRect(530, 0, 271, 461))
        self.label_imagen.setStyleSheet(u"border-image: url(:/cct/fondoLogin.jpg);")
        self.label_icono = QLabel(self.centralwidget)
        self.label_icono.setObjectName(u"label_icono")
        self.label_icono.setGeometry(QRect(45, 14, 71, 71))
        self.label_icono.setStyleSheet(u"border-image: url(:/cct/login.png);")
        self.button_register = QPushButton(self.centralwidget)
        self.button_register.setObjectName(u"button_register")
        self.button_register.setGeometry(QRect(220, 370, 131, 31))
        self.button_register.setStyleSheet(u"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(85, 170, 255, 255));\n"
"font: 700 12pt \"Tahoma\";\n"
"color: white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QMenuBar(MainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_bar.setStyleSheet(u"QMenuBar{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"}")
        self.menu_ayuda = QMenu(self.menu_bar)
        self.menu_ayuda.setObjectName(u"menu_ayuda")
        self.menu_archivo = QMenu(self.menu_bar)
        self.menu_archivo.setObjectName(u"menu_archivo")
        self.menuEditar = QMenu(self.menu_bar)
        self.menuEditar.setObjectName(u"menuEditar")
        self.menu_idioma = QMenu(self.menu_bar)
        self.menu_idioma.setObjectName(u"menu_idioma")
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.menu_bar.addAction(self.menu_archivo.menuAction())
        self.menu_bar.addAction(self.menuEditar.menuAction())
        self.menu_bar.addAction(self.menu_idioma.menuAction())
        self.menu_bar.addAction(self.menu_ayuda.menuAction())
        self.menu_ayuda.addAction(self.action_acerca_de)
        self.menu_archivo.addAction(self.action_cerrar)
        self.menuEditar.addAction(self.action_limpiar_celdas)
        self.menu_idioma.addAction(self.action_espannol)
        self.menu_idioma.addAction(self.action_ingles)

        self.line_edit_contrasenna.setPlaceholderText("Escriba aquí su contraseña...") 
        self.line_edit_usuario.setPlaceholderText("Escriba aquí su nombre de usuario...") 

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_limpiar_celdas.setText(QCoreApplication.translate("MainWindow", u"Limpiar Campos", None))
        self.action_acerca_de.setText(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.action_espannol.setText(QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.action_ingles.setText(QCoreApplication.translate("MainWindow", u"Ingl\u00e9s", None))
        self.action_cerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.button_inicio.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.label_nombre_usuario.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DE USUARIO", None))
        self.line_edit_usuario.setText("")
        self.label_titulo.setText(QCoreApplication.translate("MainWindow", u"La Estanter\u00eda de Don Librote", None))
        self.label_contrasenna.setText(QCoreApplication.translate("MainWindow", u"CONTRASE\u00d1A", None))
        self.label_subtitulo.setText(QCoreApplication.translate("MainWindow", u"INICIAR SESI\u00d3N", None))
        self.label_imagen.setText("")
        self.label_icono.setText("")
        self.button_register.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.menu_ayuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.menu_archivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuEditar.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.menu_idioma.setTitle(QCoreApplication.translate("MainWindow", u"Idioma", None))
    # retranslateUi

