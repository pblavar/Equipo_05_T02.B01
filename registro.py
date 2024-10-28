# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
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

import img.logoLogin_rc
import img.fondoLogin_rc

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
        self.action_cerrar = QAction(MainWindow)
        self.action_cerrar.setObjectName(u"action_cerrar")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.action_limpiar_campo = QAction(MainWindow)
        self.action_limpiar_campo.setObjectName(u"action_limpiar_campo")
        self.action_espannol = QAction(MainWindow)
        self.action_espannol.setObjectName(u"action_espannol")
        self.action_ingles = QAction(MainWindow)
        self.action_ingles.setObjectName(u"action_ingles")
        self.action_acerca_de = QAction(MainWindow)
        self.action_acerca_de.setObjectName(u"action_acerca_de")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_icono = QLabel(self.centralwidget)
        self.label_icono.setObjectName(u"label_icono")
        self.label_icono.setGeometry(QRect(45, 14, 71, 71))
        self.label_icono.setStyleSheet(u"border-image: url(:/cct/login.png);")
        self.line_edit_contrasenna = QLineEdit(self.centralwidget)
        self.line_edit_contrasenna.setObjectName(u"line_edit_contrasenna")
        self.line_edit_contrasenna.setGeometry(QRect(60, 300, 181, 22))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        self.line_edit_contrasenna.setFont(font)
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
        self.label_contrasenna = QLabel(self.centralwidget)
        self.label_contrasenna.setObjectName(u"label_contrasenna")
        self.label_contrasenna.setGeometry(QRect(60, 270, 91, 16))
        self.label_contrasenna.setStyleSheet(u"font: 700 10pt \"Tahoma\";\n"
"color: rgb(0, 0, 0);")
        self.line_usuario = QFrame(self.centralwidget)
        self.line_usuario.setObjectName(u"line_usuario")
        self.line_usuario.setGeometry(QRect(60, 220, 181, 10))
        self.line_usuario.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.line_usuario.setFrameShape(QFrame.Shape.HLine)
        self.line_usuario.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_titulo = QLabel(self.centralwidget)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(125, 22, 361, 51))
        self.label_titulo.setStyleSheet(u"font: 700 18pt \"Tahoma\";\n"
"color: rgb(0, 0, 0);")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_contrasenna = QFrame(self.centralwidget)
        self.line_contrasenna.setObjectName(u"line_contrasenna")
        self.line_contrasenna.setGeometry(QRect(60, 320, 181, 10))
        self.line_contrasenna.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.line_contrasenna.setFrameShape(QFrame.Shape.HLine)
        self.line_contrasenna.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_subtitulo = QLabel(self.centralwidget)
        self.label_subtitulo.setObjectName(u"label_subtitulo")
        self.label_subtitulo.setGeometry(QRect(60, 100, 301, 41))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_subtitulo.setFont(font1)
        self.label_subtitulo.setStyleSheet(u"font: 700 16pt \"Tahoma\";\n"
"color: rgb(0, 0, 0);")
        self.label_usuario = QLabel(self.centralwidget)
        self.label_usuario.setObjectName(u"label_usuario")
        self.label_usuario.setGeometry(QRect(60, 170, 151, 16))
        self.label_usuario.setStyleSheet(u"font: 700 10pt \"Tahoma\";\n"
"color: rgb(0, 0, 0);")
        self.button_aceptar = QPushButton(self.centralwidget)
        self.button_aceptar.setObjectName(u"button_aceptar")
        self.button_aceptar.setGeometry(QRect(60, 370, 131, 31))
        self.button_aceptar.setStyleSheet(u"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(85, 170, 255, 255));\n"
"font: 700 12pt \"Tahoma\";\n"
"color: white;")
        self.line_edit_usuario = QLineEdit(self.centralwidget)
        self.line_edit_usuario.setObjectName(u"line_edit_usuario")
        self.line_edit_usuario.setGeometry(QRect(60, 200, 181, 22))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setKerning(True)
        self.line_edit_usuario.setFont(font2)
        self.line_edit_usuario.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(247, 247, 247);\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: gray;\n"
"}")
        self.line_edit_email = QLineEdit(self.centralwidget)
        self.line_edit_email.setObjectName(u"line_edit_email")
        self.line_edit_email.setGeometry(QRect(280, 200, 181, 22))
        self.line_edit_email.setFont(font2)
        self.line_edit_email.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(247, 247, 247);\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: gray;\n"
"}")
        self.label_confirmar_contrasenna = QLabel(self.centralwidget)
        self.label_confirmar_contrasenna.setObjectName(u"label_confirmar_contrasenna")
        self.label_confirmar_contrasenna.setGeometry(QRect(280, 270, 181, 16))
        self.label_confirmar_contrasenna.setStyleSheet(u"font: 700 10pt \"Tahoma\";\n"
"color: rgb(0, 0, 0);")
        self.line_email = QFrame(self.centralwidget)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setGeometry(QRect(280, 220, 181, 10))
        self.line_email.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.line_email.setFrameShape(QFrame.Shape.HLine)
        self.line_email.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_confirmar_contrasenna = QFrame(self.centralwidget)
        self.line_confirmar_contrasenna.setObjectName(u"line_confirmar_contrasenna")
        self.line_confirmar_contrasenna.setGeometry(QRect(280, 320, 181, 10))
        self.line_confirmar_contrasenna.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.line_confirmar_contrasenna.setFrameShape(QFrame.Shape.HLine)
        self.line_confirmar_contrasenna.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_email = QLabel(self.centralwidget)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(280, 170, 161, 16))
        self.label_email.setStyleSheet(u"font: 700 10pt \"Tahoma\";\n"
"color: rgb(0, 0, 0);")
        self.line_edit_confirmar_contrasenna = QLineEdit(self.centralwidget)
        self.line_edit_confirmar_contrasenna.setObjectName(u"line_edit_confirmar_contrasenna")
        self.line_edit_confirmar_contrasenna.setGeometry(QRect(280, 300, 181, 22))
        self.line_edit_confirmar_contrasenna.setFont(font)
        self.line_edit_confirmar_contrasenna.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(247, 247, 247);\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: gray;\n"
"}")
        self.line_edit_confirmar_contrasenna.setEchoMode(QLineEdit.EchoMode.Password)
        self.button_volver = QPushButton(self.centralwidget)
        self.button_volver.setObjectName(u"button_volver")
        self.button_volver.setGeometry(QRect(220, 370, 131, 31))
        self.button_volver.setStyleSheet(u"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(85, 170, 255, 255));\n"
"font: 700 12pt \"Tahoma\";\n"
"color: white;")
        self.label_imagen = QLabel(self.centralwidget)
        self.label_imagen.setObjectName(u"label_imagen")
        self.label_imagen.setGeometry(QRect(530, 0, 271, 461))
        self.label_imagen.setStyleSheet(u"border-image: url(:/cct/fondoLogin.jpg);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.menu_bar = QMenuBar(MainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_archivo = QMenu(self.menu_bar)
        self.menu_archivo.setObjectName(u"menu_archivo")
        self.menu_editar = QMenu(self.menu_bar)
        self.menu_editar.setObjectName(u"menu_editar")
        self.menu_ayuda = QMenu(self.menu_bar)
        self.menu_ayuda.setObjectName(u"menu_ayuda")
        self.menu_idioma = QMenu(self.menu_bar)
        self.menu_idioma.setObjectName(u"menu_idioma")
        MainWindow.setMenuBar(self.menu_bar)

        self.menu_bar.addAction(self.menu_archivo.menuAction())
        self.menu_bar.addAction(self.menu_editar.menuAction())
        self.menu_bar.addAction(self.menu_idioma.menuAction())
        self.menu_bar.addAction(self.menu_ayuda.menuAction())
        self.menu_archivo.addAction(self.action_cerrar)
        self.menu_editar.addAction(self.action_limpiar_campo)
        self.menu_ayuda.addAction(self.action_acerca_de)
        self.menu_idioma.addAction(self.action_espannol)
        self.menu_idioma.addAction(self.action_ingles)

        self.line_edit_contrasenna.setPlaceholderText("Escriba su contraseña") 
        self.line_edit_usuario.setPlaceholderText("Escriba su nombre de usuario")
        self.line_edit_confirmar_contrasenna.setPlaceholderText("Confirme su contraseña")
        self.line_edit_email.setPlaceholderText("Escriba su correo electrónico")

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_cerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.action_limpiar_campo.setText(QCoreApplication.translate("MainWindow", u"Limpiar Campo", None))
        self.action_espannol.setText(QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.action_ingles.setText(QCoreApplication.translate("MainWindow", u"Ingl\u00e9s", None))
        self.action_acerca_de.setText(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.label_icono.setText("")
        self.label_contrasenna.setText(QCoreApplication.translate("MainWindow", u"CONTRASE\u00d1A", None))
        self.label_titulo.setText(QCoreApplication.translate("MainWindow", u"La Estanter\u00eda de Don Librote", None))
        self.label_subtitulo.setText(QCoreApplication.translate("MainWindow", u"CREAR UNA NUEVA CUENTA", None))
        self.label_usuario.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DE USUARIO", None))
        self.button_aceptar.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_confirmar_contrasenna.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR CONTRASE\u00d1A", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"CORREO ELECTR\u00d3NICO", None))
        self.button_volver.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.label_imagen.setText("")
        self.menu_archivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menu_editar.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.menu_ayuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.menu_idioma.setTitle(QCoreApplication.translate("MainWindow", u"Idioma", None))
    # retranslateUi

