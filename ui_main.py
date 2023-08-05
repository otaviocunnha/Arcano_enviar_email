# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 570)
        icon = QIcon()
        icon.addFile(u":/icons/icon/launching.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(47, 47, 47);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setPointSize(7)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 200))
        self.label_2.setMargin(0)
        self.label_2.setIndent(4)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 15))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setMouseTracking(True)
        self.label.setFocusPolicy(Qt.WheelFocus)
        self.label.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"\n"
"")
        self.label.setLineWidth(1)
        self.label.setMargin(3)

        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)


        self.verticalLayout_7.addWidget(self.frame)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabWidget = QTabWidget(self.frame_6)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"\n"
"\n"
"")
        self.editar = QWidget()
        self.editar.setObjectName(u"editar")
        self.verticalLayout_2 = QVBoxLayout(self.editar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.editar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: Arial;\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"}\n"
"QLineEdit { \n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: Arial;\n"
"    color: black;\n"
"	border: 1px solid gray; \n"
"}\n"
"\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(231, 231, 231);\n"
"	\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: Arial;\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"}\n"
"\n"
"QTextEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: Arial;\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.text_email = QLineEdit(self.frame_2)
        self.text_email.setObjectName(u"text_email")
        self.text_email.setMinimumSize(QSize(0, 0))
        self.text_email.setMaximumSize(QSize(16777215, 22))
        self.text_email.setStyleSheet(u"border-radius: 5px;")
        self.text_email.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.text_email, 0, 0, 1, 1)

        self.escolha_acao = QComboBox(self.frame_2)
        self.escolha_acao.addItem(u"")
        self.escolha_acao.addItem("")
        self.escolha_acao.addItem("")
        self.escolha_acao.addItem("")
        self.escolha_acao.setObjectName(u"escolha_acao")
        self.escolha_acao.setMaximumSize(QSize(16777215, 22))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.escolha_acao.setFont(font2)

        self.gridLayout_3.addWidget(self.escolha_acao, 1, 0, 1, 1)

        self.escolha_unidade = QComboBox(self.frame_2)
        self.escolha_unidade.addItem("")
        self.escolha_unidade.addItem("")
        self.escolha_unidade.addItem("")
        self.escolha_unidade.addItem("")
        self.escolha_unidade.setObjectName(u"escolha_unidade")
        self.escolha_unidade.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_3.addWidget(self.escolha_unidade, 2, 0, 1, 1)

        self.btn_consulta = QPushButton(self.frame_2)
        self.btn_consulta.setObjectName(u"btn_consulta")
        self.btn_consulta.setMinimumSize(QSize(0, 0))
        self.btn_consulta.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.btn_consulta.setFont(font3)
        self.btn_consulta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consulta.setStyleSheet(u"QPushButton:hover {\n"
"  background-color: #55aaff;\n"
"  border: 1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    color: #000000;\n"
"	background-color: rgb(244, 244, 0);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.btn_consulta, 3, 0, 1, 1)

        self.text_consult = QTextEdit(self.frame_2)
        self.text_consult.setObjectName(u"text_consult")
        self.text_consult.setMaximumSize(QSize(16777215, 200))

        self.gridLayout_3.addWidget(self.text_consult, 4, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.tabWidget.addTab(self.editar, "")
        self.email = QWidget()
        self.email.setObjectName(u"email")
        self.verticalLayout_3 = QVBoxLayout(self.email)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.email)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: rgb(231, 231, 231);\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(500, 500))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.atualizacao = QTextEdit(self.frame_3)
        self.atualizacao.setObjectName(u"atualizacao")
        self.atualizacao.setMinimumSize(QSize(0, 60))
        self.atualizacao.setMaximumSize(QSize(300, 60))
        self.atualizacao.setSizeIncrement(QSize(0, 0))
        self.atualizacao.setBaseSize(QSize(0, 0))
        self.atualizacao.setStyleSheet(u"QTextEdit { \n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: Arial;\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"}")

        self.gridLayout.addWidget(self.atualizacao, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.email)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QLineEdit { \n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: Arial;\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"}\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(231, 231, 231);\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(8, 0, 8, 0)
        self.planilha_2 = QLineEdit(self.frame_5)
        self.planilha_2.setObjectName(u"planilha_2")
        self.planilha_2.setMaximumSize(QSize(16777215, 22))
        self.planilha_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.planilha_2, 1, 0, 1, 1)

        self.planilha_1 = QLineEdit(self.frame_5)
        self.planilha_1.setObjectName(u"planilha_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(20)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.planilha_1.sizePolicy().hasHeightForWidth())
        self.planilha_1.setSizePolicy(sizePolicy1)
        self.planilha_1.setMinimumSize(QSize(0, 0))
        self.planilha_1.setMaximumSize(QSize(16777215, 22))
        self.planilha_1.setStyleSheet(u"QLineEdit { \n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: Arial;\n"
"    color: black;\n"
"}")
        self.planilha_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.planilha_1, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.planilha_3 = QLineEdit(self.frame_5)
        self.planilha_3.setObjectName(u"planilha_3")
        self.planilha_3.setMaximumSize(QSize(16777215, 22))
        self.planilha_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.planilha_3, 2, 0, 1, 2)

        self.btnExecute = QPushButton(self.frame_5)
        self.btnExecute.setObjectName(u"btnExecute")
        self.btnExecute.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        self.btnExecute.setFont(font5)
        self.btnExecute.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnExecute.setStyleSheet(u"QPushButton:hover {\n"
"  background-color: #55aaff;\n"
"  border: 1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  color: #000000;\n"
"	border: 1px solid gray; \n"
"	background-color: rgb(244, 244, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.btnExecute, 3, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.tabWidget.addTab(self.email, "")
        self.outros = QWidget()
        self.outros.setObjectName(u"outros")
        self.verticalLayout = QVBoxLayout(self.outros)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.outros)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 6)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.horizontalLayout_2.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.atualizacao_2 = QTextEdit(self.frame_4)
        self.atualizacao_2.setObjectName(u"atualizacao_2")
        self.atualizacao_2.setMinimumSize(QSize(0, 60))
        self.atualizacao_2.setMaximumSize(QSize(300, 60))
        self.atualizacao_2.setStyleSheet(u"QTextEdit { \n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: Arial;\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"}")

        self.horizontalLayout_2.addWidget(self.atualizacao_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_7 = QFrame(self.outros)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QLineEdit { \n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: Arial;\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"}\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(231, 231, 231);\n"
"\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.planilha_telmac = QLineEdit(self.frame_7)
        self.planilha_telmac.setObjectName(u"planilha_telmac")
        self.planilha_telmac.setMaximumSize(QSize(16777215, 22))
        self.planilha_telmac.setStyleSheet(u"QLineEdit { \n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: Arial;\n"
"    color: black;\n"
"}")
        self.planilha_telmac.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.planilha_telmac)

        self.planilha_fparts = QLineEdit(self.frame_7)
        self.planilha_fparts.setObjectName(u"planilha_fparts")
        self.planilha_fparts.setMaximumSize(QSize(16777215, 22))
        self.planilha_fparts.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.planilha_fparts)

        self.planilha_rsg = QLineEdit(self.frame_7)
        self.planilha_rsg.setObjectName(u"planilha_rsg")
        self.planilha_rsg.setMaximumSize(QSize(16777215, 22))
        self.planilha_rsg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.planilha_rsg)

        self.btn_send_email = QPushButton(self.frame_7)
        self.btn_send_email.setObjectName(u"btn_send_email")
        self.btn_send_email.setMaximumSize(QSize(16777215, 50))
        self.btn_send_email.setFont(font5)
        self.btn_send_email.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_send_email.setStyleSheet(u"QPushButton:hover {\n"
"  background-color: #55aaff;\n"
"  border: 1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  color: #000000;\n"
"	border: 1px solid gray; \n"
"	background-color: rgb(244, 244, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.btn_send_email)


        self.verticalLayout.addWidget(self.frame_7)

        self.tabWidget.addTab(self.outros, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font6 = QFont()
        font6.setBold(True)
        self.label_4.setFont(font6)

        self.verticalLayout_7.addWidget(self.label_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cyber Sistem", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icon/launching.png\" width=\"50\" height=\"50\"/><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">ARCANO</span></p></body></html>", None))
        self.label_6.setText("")
        self.text_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email ", None))
        self.escolha_acao.setItemText(1, QCoreApplication.translate("MainWindow", u"adicionar", None))
        self.escolha_acao.setItemText(2, QCoreApplication.translate("MainWindow", u"remover", None))
        self.escolha_acao.setItemText(3, QCoreApplication.translate("MainWindow", u"Ver e-mails cadastrados", None))

        self.escolha_acao.setCurrentText("")
        self.escolha_unidade.setItemText(0, "")
        self.escolha_unidade.setItemText(1, QCoreApplication.translate("MainWindow", u"edit_Nome_1_txt", None))
        self.escolha_unidade.setItemText(2, QCoreApplication.translate("MainWindow", u"edit_Nome_2_txt", None))
        self.escolha_unidade.setItemText(3, QCoreApplication.translate("MainWindow", u"edit_Nome_3_txt", None))

#if QT_CONFIG(tooltip)
        self.btn_consulta.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enviar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_consulta.setText(QCoreApplication.translate("MainWindow", u"Editar / Consultar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editar), QCoreApplication.translate("MainWindow", u"Editar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enviar despesas por e-mail", None))
        self.atualizacao.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">STATUS</p></body></html>", None))
        self.planilha_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Caminho da planilha Gastos Hotel", None))
        self.planilha_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Caminho da Planilha Gastos Aereo ", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00ba Fatura Aereo", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00ba Fatura Hotel", None))
        self.planilha_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Caminho da Planilha gastos Fatura", None))
        self.btnExecute.setText(QCoreApplication.translate("MainWindow", u"Enviar e-mail j\u00e1 pr\u00e9 definido", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.email), QCoreApplication.translate("MainWindow", u"E-mail Agro", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enviar despesas por e-mail</p></body></html>", None))
        self.atualizacao_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">STATUS</p></body></html>", None))
        self.planilha_telmac.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Caminho da Planilha 1", None))
        self.planilha_fparts.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Caminho da Planilha 2", None))
        self.planilha_rsg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Caminho da Planilha 3", None))
        self.btn_send_email.setText(QCoreApplication.translate("MainWindow", u"Enviar e-mail j\u00e1 pr\u00e9 definido", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.outros), QCoreApplication.translate("MainWindow", u"E-mail Outros", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Vers\u00e3o: 2023", None))
    # retranslateUi

