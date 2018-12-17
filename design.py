# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(404, 683)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.songText = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.songText.setFont(font)
        self.songText.setReadOnly(True)
        self.songText.setObjectName("songText")
        self.verticalLayout.addWidget(self.songText)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.spinBox = QtWidgets.QSpinBox(self.splitter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(15)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.splitter)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.similarWord = QtWidgets.QLineEdit(self.centralwidget)
        self.similarWord.setObjectName("similarWord")
        self.verticalLayout.addWidget(self.similarWord)
        self.btnFind = QtWidgets.QPushButton(self.centralwidget)
        self.btnFind.setObjectName("btnFind")
        self.verticalLayout.addWidget(self.btnFind)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "We Will Rock You"))
        self.label.setText(_translate("mainWindow", "Параметры:"))
        self.label_2.setText(_translate("mainWindow", "Количество элементов для вывода"))
        self.checkBox.setText(_translate("mainWindow", "Выводить информацию о степени сходства"))
        self.label_3.setText(_translate("mainWindow", "Фраза для поиска"))
        self.btnFind.setText(_translate("mainWindow", "Поиск"))

