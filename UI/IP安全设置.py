# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IP安全设置.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.resize(491, 350)
        self.label_2 = QtWidgets.QLabel(Dialog3)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog3)
        self.lineEdit.setGeometry(QtCore.QRect(190, 250, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog3)
        self.textBrowser.setGeometry(QtCore.QRect(55, 40, 391, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog3)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 310, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog3)
        self.label.setGeometry(QtCore.QRect(50, 250, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog3)
        self.pushButton.setGeometry(QtCore.QRect(110, 310, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog3)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 310, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog3)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi(self, Dialog3):
        _translate = QtCore.QCoreApplication.translate
        Dialog3.setWindowTitle(_translate("Dialog3", "IP安全设置"))
        self.label_2.setText(_translate("Dialog3", "已被拦截IP地址"))
        self.pushButton_2.setText(_translate("Dialog3", "取消"))
        self.label.setText(_translate("Dialog3", "拦截IP地址设置："))
        self.pushButton.setText(_translate("Dialog3", "添加"))
        self.pushButton_3.setText(_translate("Dialog3", "删除"))

