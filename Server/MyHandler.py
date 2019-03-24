from pyftpdlib.handlers import FTPHandler#控制用户的连接
import configparser
import os
from pyftpdlib.filesystems import AbstractedFS
class myHandler(FTPHandler):

    def getconfig(self,string):#获得相应option段的内容
        config = configparser.ConfigParser()
        config.read('./ip.ini')
        return config.get('ipset',string)

    def get_connconfig(self,string):
        config = configparser.ConfigParser()
        config.read('./ipconn.ini')
        return config.get('ipset', string)

    def isconfig(self,string):#判断ftpset中是否存在string段
        config = configparser.ConfigParser()
        config.read('./ip.ini')
        return config.has_option('ipset',string)

    def conn_isconfig(self,string):
        config = configparser.ConfigParser()
        config.read('./ipconn.ini')
        return config.has_option('ipset', string)

    def writeconfig(self,string):#将string写入conn_ip中
        try:
            config = configparser.ConfigParser()
            config.add_section('ipset')
            config.set('ipset','conn_ip',str(string))
            with open('./ipconn.ini','w+') as conf:
                config.write(conf)
        except Exception as e:
            print(str(e))

    def getfile(self,num):
        try:
            config = configparser.ConfigParser()
            config.read('./file.ini')
            return config.get('flow',num)
        except Exception as e:
            print(str(e))

    #上传流量
    def writeint(self,num):
        try:
            config = configparser.ConfigParser()
            config.add_section('flow')
            config.set('flow','uploading',str(num))
            config.set('flow','download',self.getfile('download'))
            with open('./file.ini','w+') as f:
                config.write(f)
        except Exception as e:
            print(str(e))

    #下载流量
    def upint(self,num):
        try:
            config = configparser.ConfigParser()
            config.add_section('flow')
            config.set('flow','uploading',self.getfile('uploading'))
            config.set('flow','download',str(num))
            with open('./file.ini','w+') as f:
                config.write(f)
        except Exception as e:
            print(str(e))

    def on_connect(self):  # 链接时调用#导入链接时的判断语句，即针对限制ip的筛选来进行将限制ip服务链接关闭的功能
        try:
            if self.isconfig('limit_ip'):
                strings = self.getconfig('limit_ip')
                lists = strings.split(';')#判断限制ip是否在连接
                if self.remote_ip in lists:
                    self.close()#若限制ip在连接中，则关闭此ip的连接
                else:#否则则将该已连接ip加入配置文件中，用以在主界面的显示
                    self.writeconfig(str(self.remote_ip+';'))
            else:
                self.writeconfig(str(self.remote_ip+';'))
        except Exception as e:
            print(str(e))

    def on_disconnect(self):  # 关闭连接是调用,将conn_ip中的内容删去此时连接的ip地址
        try:
            strings = str(self.get_connconfig('conn_ip'))
            lists = strings.split(';')#找出已经连接ip地址的记录
            if self.remote_ip in lists:
                lists.remove(self.remote_ip)#当对应ip停止连接时，会在ipset配置文件中删除掉已连接的ip地址
                self.writeconfig(';'.join(lists))
            else:
                self.writeconfig(';'.join(lists))
        except Exception as e:
            print(str(e))


    def on_login(self, username):  # 登录时调用
        # do something when user login
        pass

    def on_logout(self, username):  # 登出时调用
        # do something when user logs out
        pass

    def on_file_sent(self, file):  # 文件下载后调用
        # do something when a file has been sent
        try:
            dowmload = int(os.path.getsize(file))#获取下载文件的大小，并且储存在一个int变量中
            newsize = int(dowmload +int(self.getfile('download')))
            self.upint(newsize)
        except Exception as e:
            print(str(e))

    def on_file_received(self, file):  # 文件上传后调用
        # do something when a file has been received
        try:
            uploading = int(os.path.getsize(file))  # 获取下载文件的大小，并且储存在一个int变量中
            newsize = int(uploading + int(self.getfile('uploading')))
            self.writeint(newsize)
        except Exception as e:
            print(str(e))

    def on_incomplete_file_sent(self, file):  # 下载文件时调用
        # do something when a file is partially sent
        pass


    def on_incomplete_file_received(self, file):  # 上传文件时调用
        # remove partially uploaded files
       pass