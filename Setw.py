import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import configparser#导入配置文件包
from UI.服务器配置信息 import *
import socket
from UI.本机IP地址 import *


#定义获取本机IP地址界面
class Getip_w(QDialog,Ui_Dialog5):
    def __init__(self):
        QDialog.__init__(self,parent=None)
        self.setupUi(self)
        for i in self.getIPlist():
            self.textEdit.append(i)
    #获取本机IP地址
    def getIPlist(self):
        iplist=socket.gethostbyname_ex(socket.gethostname())[2]
        return iplist



#定义服务器配置参数页面的类
class Set_Window(QDialog,Ui_Dialog1):
    def __init__(self):
        QDialog.__init__(self,parent=None)
        self.setupUi(self)

    #设定浏览按键，返回文件浏览目录的函数
    def setBrowerPath(self):
        try:
            download_path = QFileDialog.getExistingDirectory(self,'浏览','D:/Desktop/FTP_Server')
            return download_path
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))


    @pyqtSlot()
    def on_pushButton_clicked(self):
        try:
            ipw = Getip_w()
            ipw.exec_()
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        try:
            #将文本框全部置空
            self.lineEdit.setText('')
            self.lineEdit_9.setText('')
            self.lineEdit_8.setText('')
            self.lineEdit_7.setText('')
            self.lineEdit_6.setText('')
            self.lineEdit_5.setText('')
            self.lineEdit_4.setText('')
            self.lineEdit_3.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit.setText('')
            self.close()
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        try:
            self.lineEdit_4.setText(self.setBrowerPath())

        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

    #定义启动服务器按钮功能作用
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        global t
        try:
            if str(self.lineEdit.text())=='' or str(self.lineEdit_2.text())==''or str(self.lineEdit_3.text())=='' or str(self.lineEdit_4.text())=='' or str(self.lineEdit_7.text())=='' or str(self.lineEdit_8.text())=='' or self.lineEdit_5.text()=='' or self.lineEdit_6.text()=='' or self.lineEdit_9.text()=='':
            # 新建一个服务器设置对象
                QMessageBox.information(self,'提示','输入不能为空！')
            else:
                #fserver = ftpServer(str(self.lineEdit.text()), str(self.lineEdit_2.text()),
                 #                    str(self.lineEdit_3.text()),
                  #                   str(self.lineEdit_4.text()), int(self.lineEdit_8.text()), int(self.lineEdit_7.text()),
                   ##                   int(self.lineEdit_5.text()), int(self.lineEdit_6.text()), str(self.lineEdit_9.text()))
                #把ftp启动配置信息写入配置文件，这个配置信息是由gui页面输入得到的
                config =configparser.ConfigParser()
                config.add_section('ftpset')
                config.set('ftpset','address',str(self.lineEdit.text()))
                config.set('ftpset','user',str(self.lineEdit_2.text()))
                config.set('ftpset','password',str(self.lineEdit_3.text()))
                config.set('ftpset','filepath',str(self.lineEdit_4.text()))
                config.set('ftpset','portnumber',(self.lineEdit_5.text()))
                config.set('ftpset','maxcnn',(self.lineEdit_6.text()))
                config.set('ftpset','speeddown',(self.lineEdit_7.text()))
                config.set('ftpset','speedup',str(self.lineEdit_8.text()))
                config.set('ftpset','msg',str(self.lineEdit_9.text()))
                config.set('ftpset', 'staus', '1')  # 设置配置文件是否配置文件保存成功，保存成功则状态为1，即配置文件已有内容
                with open('config.ini','w') as conf:
                    config.write(conf)
                QMessageBox.information(self, '提示', '配置文件保存成功!')
                time.sleep(1)
                self.close()

        except Exception as e:
            QMessageBox.information(self,'错误',str(e))
