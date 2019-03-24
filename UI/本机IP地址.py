# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '本机IP地址.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog5(object):
    def setupUi(self, Dialog5):
        Dialog5.setObjectName("Dialog5")
        Dialog5.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(Dialog5)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 381, 271))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog5)
        QtCore.QMetaObject.connectSlotsByName(Dialog5)

    def retranslateUi(self, Dialog5):
        _translate = QtCore.QCoreApplication.translate
        Dialog5.setWindowTitle(_translate("Dialog5", "本机IP地址"))

