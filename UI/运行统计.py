# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '运行统计.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(400, 300)
        self.label_2 = QtWidgets.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 54, 12))
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog2)
        self.textBrowser_2.setGeometry(QtCore.QRect(100, 190, 241, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog2)
        self.textBrowser.setGeometry(QtCore.QRect(100, 50, 241, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(160, 20, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog2)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 54, 12))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog2)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 100, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog2)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 240, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog2)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 240, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(Dialog2)
        self.line.setGeometry(QtCore.QRect(0, 130, 401, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "运行统计"))
        self.label_2.setText(_translate("Dialog2", "上传："))
        self.label.setText(_translate("Dialog2", "统计流量信息"))
        self.label_3.setText(_translate("Dialog2", "下载："))
        self.pushButton.setText(_translate("Dialog2", "刷新"))
        self.pushButton_2.setText(_translate("Dialog2", "清空"))
        self.pushButton_3.setText(_translate("Dialog2", "清空"))
        self.pushButton_4.setText(_translate("Dialog2", "刷新"))

