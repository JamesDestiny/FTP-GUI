# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '服务器配置信息.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(484, 513)
        self.label_2 = QtWidgets.QLabel(Dialog1)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_9.setGeometry(QtCore.QRect(150, 380, 161, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_9 = QtWidgets.QLabel(Dialog1)
        self.label_9.setGeometry(QtCore.QRect(30, 380, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_8.setGeometry(QtCore.QRect(150, 340, 161, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_7.setGeometry(QtCore.QRect(150, 300, 161, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_3 = QtWidgets.QLabel(Dialog1)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 100, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(Dialog1)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog1)
        self.label.setGeometry(QtCore.QRect(30, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(Dialog1)
        self.label_6.setGeometry(QtCore.QRect(30, 260, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog1)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(64, 440, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog1)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 440, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(Dialog1)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 140, 161, 20))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 180, 161, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 220, 161, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 260, 161, 20))
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(Dialog1)
        self.pushButton.setGeometry(QtCore.QRect(330, 60, 151, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(Dialog1)
        self.label_8.setGeometry(QtCore.QRect(30, 340, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Dialog1)
        self.label_7.setGeometry(QtCore.QRect(30, 300, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog1)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 180, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "服务器配置信息"))
        self.label_2.setText(_translate("Dialog1", "用户名："))
        self.lineEdit_9.setPlaceholderText(_translate("Dialog1", "默认：连接成功"))
        self.label_9.setText(_translate("Dialog1", "连接提示字符串："))
        self.lineEdit_8.setPlaceholderText(_translate("Dialog1", "单位：kb/s"))
        self.lineEdit_7.setPlaceholderText(_translate("Dialog1", "单位：kb/s"))
        self.label_3.setText(_translate("Dialog1", "密码："))
        self.label_5.setText(_translate("Dialog1", "端口号："))
        self.label.setText(_translate("Dialog1", "服务器IP地址："))
        self.label_6.setText(_translate("Dialog1", "最大同时连接数："))
        self.pushButton_3.setText(_translate("Dialog1", "保存配置文件"))
        self.pushButton_4.setText(_translate("Dialog1", "取消"))
        self.label_4.setText(_translate("Dialog1", "登录目录选择："))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog1", "默认21"))
        self.lineEdit_6.setPlaceholderText(_translate("Dialog1", "默认512"))
        self.pushButton.setText(_translate("Dialog1", "本机局域网内IP地址查询"))
        self.label_8.setText(_translate("Dialog1", "客户端上传速度："))
        self.label_7.setText(_translate("Dialog1", "客户端下载速度："))
        self.pushButton_2.setText(_translate("Dialog1", "浏览"))

