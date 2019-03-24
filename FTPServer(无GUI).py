import os

from Server.MyHandler import *


def main():
    ##添加用户对象以及组
    authorizer = DummyAuthorizer()
    authorizer.add_user('user','123456',os.getcwd(),perm='elradfmwMT')
    #authorizer.add_anonymous(os.getcwd())#添加对象到虚拟用户组中


    ##通过设置数据计数器的大小来达到限速的效果
    dtp_handler = ThrottledDTPHandler
    dtp_handler.read_limit = 30720 #30kb/s(30x1024)  即接收的最大速度，代表着客户端上传的最大速度
    dtp_handler.write_limit = 30720 #即发送的最大速度，代表着客户端下载的最大速度

    # 设置服务器对象，将用户以及数据控制器与服务器对象进行绑定
    ftp_handler = myHandler
    ftp_handler.dtp_handler = dtp_handler
    ftp_handler.authorizer = authorizer
    ftp_handler.banner="来了，老弟！"#客户连接时发送的字符串


    address = ('',21)#设置服务器信息，即IP地址和端口号
    ftp_server = FTPServer(address,ftp_handler)#绑定ftp_handler和地址信息
    ftp_server.max_cons=2 #接受的最大同时连接数 默认为512
    ftp_server.max_cons_per_ip =0 #接受的为同一IP地址接受的最大连接数默认为0==无限制

    #logging.basicConfig(filename='server.log',level=logging.INFO)#将控制台输出的日志文件通过logging保存在server.log日志文件中
    ftp_server.serve_forever()#启动异步IO循环









if __name__ == '__main__':
    main()


