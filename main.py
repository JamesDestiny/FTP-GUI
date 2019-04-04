import time
import configparser
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import threading
from Setw import Set_Window
from UI.FTP服务器端 import *
from UI.IP安全设置 import *
from UI.日志文件查看 import *
from UI.运行统计 import *
import socket
from Server.Ftp_Server import ftpServer
import inspect
import ctypes
import time


#定义日志文件查看页面的类
class Log_Window(QDialog,Ui_Dialog5):
    def __init__(self):
        QDialog.__init__(self,parent=None)
        self.setupUi(self)
        time.sleep(0.5)
        self.ReadLog()

    #定义日志文件读取函数
    def ReadLog(self):
        f = open('Log_file/All.log','r')
        try:
            while True:
                str = f.readline()
                if not str:
                    break
                else:
                    self.textBrowser.append(str)
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

#定义运行统计页面的类
class Collect_Window(QDialog,Ui_Dialog2):
    def __init__(self):
        QDialog.__init__(self,parent=None)
        self.setupUi(self)

    def getfile(self,num):
        try:
            config = configparser.ConfigParser()
            config.read('./file.ini')
            return config.get('flow',num)
        except Exception as e:
            print(str(e))

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        try:
            self.textBrowser.setText('')

        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        try:
            self.textBrowser_2.setText('')
        except Exception as e:
            QMessageBox.information(self, '错误', str(e))

    @pyqtSlot()
    def on_pushButton_clicked(self):
        try:
            self.textBrowser.setText(self.getfile('uploading')+' 字节')
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        try:
            self.textBrowser_2.setText(self.getfile('download')+' 字节')
        except Exception as e:
            QMessageBox.information(self, '错误', str(e))

#定义IP安全设置页面的类
class Ipset_Window(QDialog,Ui_Dialog3):
    def __init__(self):
        QDialog.__init__(self,parent=None)
        self.setupUi(self)
        try:
            self.textBrowser.setText(self.getlimit_ip('limit_ip'))
        except Exception as e :
            QMessageBox.information(self,'错误',str(e))

    #定义取消按钮的作用函数,输入文本框清空，然后关闭页面
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        try:
            self.lineEdit.setText('')
            self.close()
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

    #定义获取配置文件中全部限制ip地址
    def getlimit_ip(self,string):
        try:
            config = configparser.ConfigParser()
            config.read('./ip.ini')
            return config.get('ipset',string )
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

    #定义添加按钮函数的作用，将限制IP添加入配置文件中
    @pyqtSlot()
    def on_pushButton_clicked(self):
        try:
            if self.lineEdit.text() != '':
                config = configparser.ConfigParser()
                config.add_section('ipset')
                config.set('ipset','limit_ip',self.getlimit_ip('limit_ip')+';'+self.lineEdit.text())
                with open('./ip.ini', 'w') as conf:
                    config.write(conf)
                QMessageBox.information(self,'提示','添加限制ip地址成功！')
                try:
                    self.textBrowser.setText(self.getlimit_ip('limit_ip'))
                except Exception as e:
                    QMessageBox.information(self, '错误', str(e))
            else:
                QMessageBox.information(self,'错误','输入不能为空！')
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

    #定义删除按钮函数的作用，将限制ip移除出配置文件中
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        try:
            if self.lineEdit.text()!='':
                strings = str(self.getlimit_ip('limit_ip'))
                lists=strings.split(';')
                if self.lineEdit.text() in lists:
                    lists.remove(self.lineEdit.text())
                    config3 =configparser.ConfigParser()
                    config3.add_section('ipset')
                    config3.set('ipset','limit_ip',';'.join(lists))
                    with open('./ip.ini','w+') as conf:
                        config3.write(conf)
                    QMessageBox.information(self,'提示','删除成功！')
                    try:
                        self.textBrowser.setText(self.getlimit_ip('limit_ip'))
                    except Exception as e:
                        QMessageBox.information(self, '错误', str(e))
                else:
                    QMessageBox.information(self,'提示','该IP地址未被限制！请检查后再输入！')
            else:
                QMessageBox.information(self,'错误','输入不能为空！')
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))



#定义主界面的类
class mainwid(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self,parent=None)
        self.setupUi(self)
        time.sleep(1)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.f = ftpServer()
        self.t = threading.Thread(target=self.f.run)
        self.t1 = threading.Thread(target=self.f.run)
        self.t2 =threading.Thread(target=self.f.run)
        self.t3 = threading.Thread(target=self.f.run)

    #杀死ftp服务器线程
    def _async_raise(self,tid, exctype):
            """raises the exception, performs cleanup if needed"""
            tid = ctypes.c_long(tid)
            if not inspect.isclass(exctype):
                exctype = type(exctype)
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
            if res == 0:
                raise ValueError("invalid thread id")
            elif res != 1:
                # """if it returns a number greater than one, you're in trouble,
                # and you should call it again with exc=NULL to revert the effect"""
                ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
                raise SystemError("PyThreadState_SetAsyncExc failed")

    def stop_thread(self,thread):
            self._async_raise(thread.ident, SystemExit)


    #定义给文本框添加字符串的函数
    def addedit(self,string):
        self.textEdit.append(string)



    def getconfig(self,strings):
        get=configparser.ConfigParser()
        get.read('config.ini')
        return get.get('ftpset',strings)

    #定义关闭ftp服务器时，需要清空已连接ip
    def claear_conn_ip(self):
        get = configparser.ConfigParser()
        get.add_section('ipset')
        get.set('ipset','conn_ip','')
        with open('ipconn.ini','w') as f:
            get.write(f)


    #获取本机IP地址
    def getIPlist(self):
        iplist=socket.gethostbyname_ex(socket.gethostname())[2]
        return iplist

    #关闭ftp服务器的按钮
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        try:
            if self.t.is_alive() and not self.t1.is_alive() and not self.t2.is_alive() and not self.t3.is_alive():
                self.stop_thread(self.t)
            elif self.t1.is_alive() and not self.t.is_alive() and not self.t2.is_alive() and not self.t3.is_alive():
                self.stop_thread(self.t1)
            elif self.t2.is_alive() and not self.t.is_alive() and not self.t1.is_alive() and not self.t3.is_alive():
                self.stop_thread(self.t2)
            elif self.t3.is_alive() and not self.t.is_alive() and not self.t1.is_alive() and not self.t2.is_alive():
                self.stop_thread(self.t3)
            time.sleep(1)
            QMessageBox.information(self,'提示','关闭服务器成功！')
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            self.label_2.setText('控制台信息：服务器已关闭！')
            self.textBrowser.setText('')
            self.textEdit.setText('')
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))


    @pyqtSlot()
    def on_pushButton_clicked(self):
        try:
            if self.getconfig('address')!='':
                QMessageBox.information(self, '提示', '已有历史配置信息，将选用之前的配置信息来启动FTP服务器！')
                if self.getconfig('address') not in self.getIPlist():
                    QMessageBox.information(self,'提示','当前网络环境变更，请重新设置配置信息')
                    try:
                        SetW = Set_Window()
                        SetW.exec_()
                    except Exception as e:
                        QMessageBox.information(self,'错误',str(e))
                else:
                    time.sleep(1)
                    if  not self.t.is_alive() and not self.t1.is_alive() and not self.t2.is_alive() and not self.t3.is_alive():
                        self.t.start()
                        QMessageBox.information(self, '提示', '开启成功！')
                        self.outtextEdit()
                        self.label_2.setText('控制台信息：已开FTP服务器IP地址：ftp://' + self.getconfig('address'))
                    elif self.t.is_alive() and not self.t1.is_alive() and not self.t2.is_alive() and not self.t3.is_alive():
                        QMessageBox.information(self,'警告','通常每个套接字地址(协议/网络地址/端口)只允许使用一次！请重新进入程序!')
                        self.close()


                    self.pushButton.setEnabled(False)
                    self.pushButton_2.setEnabled(True)
                    self.pushButton_3.setEnabled(True)
                    self.pushButton_4.setEnabled(True)
                    self.pushButton_5.setEnabled(True)
            else:
                QMessageBox.information(self,'提示','请先配置FTP服务器信息！')
                try:
                    SetW = Set_Window()# 弹出服务器配置界面窗口
                    SetW.exec_()
                except Exception as e :
                    QMessageBox.information(self,'错误',str(e))
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))
            self.t10.start()


    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        try:
            self.textEdit.setPlainText('')
            self.Update()
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

    def outtextEdit(self):#定义输出到控制台信息的内容
        src = open('Log_file/server.log','r',encoding="utf-8",errors="ignore")
        while True:
            mystr = src.readline()
            if not mystr:
                break
            else:
                self.textEdit.append(str(mystr))

    #定义刷新函数。刷新时，将sever日志内容增加到all日志中，后清空server日志内容
    def Update(self):
        f1 = open('Log_file/server.log','r+')
        f2 = open('Log_file/All.log','a')
        try:
            while True:
                mystr = f1.readline()
                if not mystr:
                    break
                else:
                    f2.write(mystr+'\n')
            #复制完server日志文件到All日志文件后将其清空
            f1.seek(0)#定位文件，使下一个函数起作用
            f1.truncate()#清空文件
        except Exception as e :
            QMessageBox.information(self,'错误',str(e))


    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        try:
            self.outtextEdit()
            self.Update()
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

    #定义菜单栏上点击服务器日志查看时的操作
    @pyqtSlot()
    def on_actionsad_triggered(self):
        try:
            logW = Log_Window()
            logW.exec_()
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

    @pyqtSlot()
    #定义菜单栏上退出点击时的操作
    def on_actionexit_triggered(self):
        try:
            self.close()
            sys.exit()
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))

    @pyqtSlot()
    #定义菜单栏上帮助点击时的操作
    def on_actionhelp_triggered(self):
        pass
        #QApplication.processEvents()  # 屏幕刷新

        #弹出帮助界面窗口

    @pyqtSlot()
    #定义菜单栏上关于点击时的操作
    def on_actionabout_triggered(self):
        pass#弹出关于界面窗口

    @pyqtSlot()
    # 定义菜单栏上流量统计点击时的操作
    def on_actionconllect_triggered(self):
        try:
            CollectW = Collect_Window()# 弹出流量统计界面窗口
            CollectW.exec_()
        except Exception as  e:
            QMessageBox.information(self,'错误',str(e))
    @pyqtSlot()
    # 定义菜单栏上服务器配置点击时的操作
    def on_actionset_triggered(self):
        try:
            SetW = Set_Window()# 弹出服务器配置界面窗口
            SetW.exec_()
        except Exception as e :
            QMessageBox.information(self,'错误',str(e))
    @pyqtSlot()
    # 定义菜单栏上IP设置点击时的操作
    def on_actionban_triggered(self):
        try:
            IpsetW = Ipset_Window() # 弹出IP设置界面窗口
            IpsetW.exec_()

        except Exception as e :
            QMessageBox.information(self,'错误',str(e))

    def getconfig2(self,string):
        get = configparser.ConfigParser()
        get.read('ipconn.ini')
        return get.get('ipset', string)

    def isconfig(self,string):
        get = configparser.ConfigParser()
        get.read('ipconn.ini')
        return get.has_section(string)

    def isoption_in_config(self,string,strs):
        get =configparser.ConfigParser()
        get.read('ipconn.ini')
        return get.has_option(string,strs)

    def writeconfig(self,string,str=''):
        get =configparser.ConfigParser()
        get.add_section(string)
        get.set(string,str,'')
        with open('ipconn.ini','w') as conf:
            get.write(conf)
    #当前已连接ip地址的刷新
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        try:
            if self.isconfig('ipset'):
                if self.isoption_in_config('ipset','conn_ip'):
                    self.textBrowser.setText(self.getconfig2('conn_ip'))
                else:
                    self.writeconfig('ipset','conn_ip')
                    self.textBrowser.setText(self.getconfig2('conn_ip'))
            else:
                if self.isoption_in_config('ipset', 'conn_ip'):
                    self.textBrowser.setText(self.getconfig2('conn_ip'))
                else:
                    self.writeconfig('ipset','conn_ip')
                    self.textBrowser.setText(self.getconfig2('conn_ip'))
        except Exception as e:
            QMessageBox.information(self,'错误',str(e))



