import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '139.62.210.152'
PORT = 1111

s.connect((HOST, PORT))

print("Success connect to " + HOST)