import logging  # 添加日志管理功能

from PyQt5.QtWidgets import QMessageBox
from pyftpdlib.authorizers import DummyAuthorizer  # 创建虚拟用户组，添加可以连接FTP服务的用户
from pyftpdlib.handlers import ThrottledDTPHandler  # 在数据计数器中包装发送和接收，可以达到限速的效果
from pyftpdlib.servers import FTPServer  # 导入控制服务器接受者的各种信息，设置IP地址以及端口号
import threading
from Server.MyHandler import myHandler
import configparser

class ftpServer():
    def __init__(self):
        self.address =self.getconfig('address')#定义IP地址
        self.username=self.getconfig('user')#定义用户名
        self.userpd = self.getconfig('password')#定义用户密码
        self.filepath=self.getconfig('filepath')#定义文件目录
        self.speedup=int(self.getconfig('speedup'))#定义上传速度
        self.speeddown=int(self.getconfig('speeddown'))#定义下载速度
        self.number = int(self.getconfig('portnumber'))#定义端口号
        self.maxconnect=int(self.getconfig('maxcnn'))#定义最大连接数
        self.message=self.getconfig('msg')#定义发送给客户端的连接提示符

    #获取配置文件信息
    def getconfig(self,strings):
        config=configparser.ConfigParser()
        config.read('./config.ini')
        return config.get('ftpset',strings)
    #定义ftp用户组·绑定函数,返回一个用户对象
    def UserSet(self):
        #添加用户对象以及组
        authorizer = DummyAuthorizer()
        authorizer.add_user(self.username, self.userpd, self.filepath, perm='elradfmwMT')#定义连接组用户的权限以及用户名密码，和服务器连接后打开的目录
        return authorizer

    #设置服务器数据计数器大小，返回一个计数器对象
    def DataSet(self):
        dtp_handler = ThrottledDTPHandler
        dtp_handler.read_limit = int(self.speedup)*1024  # 30kb/s(30x1024)  即接收的最大速度，代表着客户端上传的最大速度
        dtp_handler.write_limit = int(self.speeddown)*1024  # 即发送的最大速度，代表着客户端下载的最大速度
        return dtp_handler

    #设置服务器对象信息，返回一个服务器对象
    def ServerSet(self):
        ftp_handler = myHandler
        ftp_handler.dtp_handler = self.DataSet()
        ftp_handler.authorizer = self.UserSet()
        ftp_handler.banner = self.message  # 客户连接成功时发送给客户端的字符串
        return ftp_handler

    #定义服务器配置信息，返回ftp_server对象
    def ServerStart(self):
        add =(self.address,self.number)#设置ip地址以及端口号
        ftp_server = FTPServer(add, self.ServerSet())  # 绑定ftp_handler和地址信息
        ftp_server.max_cons = self.maxconnect  # 接受的最大同时连接数 默认为512
        ftp_server.max_cons_per_ip = 0  # 接受的为同一IP地址接受的最大连接数默认为0==无限制
        return ftp_server

    #定义启动函数
    def run(self):
        try:
            logging.basicConfig(filename='Log_file/server.log', level=logging.INFO)  # 将控制台输出的日志文件通过logging保存在server.log日志文件中
            self.ServerStart().serve_forever()
            # 启动异步IO循环
        except Exception as e:
            print(str(e))

    #定义停止函数
    def stop(self):
        try:
            self.ServerStart().close_all()
        except Exception as e:
           QMessageBox.information(self,'错误',str(e))


if __name__=='__main__':
    f =ftpServer()
    f.run()