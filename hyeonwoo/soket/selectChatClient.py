import socket

ip = '127.0.0.1'
port = 55555
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send("Hello".encode())
data = s.recv(size)

print(data.decode())
s.close()