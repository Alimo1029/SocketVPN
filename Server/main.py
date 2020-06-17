# SocketVPN Server端
# Socket(自创仿VPN)协议
# 防VPN协议墙
# By Mr.LM


import socket

host = "localhost"
port = 28898

skServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 创建套接字

skServer.settimeout(30) # 30秒超时

skServer.bind((host,port))  # 绑定地址

skServer.listen(5)  # 设置最大挂起连接数

while True:
    A_skServer, Addr = skServer.accept()
    print(Addr)