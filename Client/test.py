import socket

skClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skClient.connect_ex(("127.0.0.1", 28898))