import socket

HOST, PORT = "localhost", 3001
data = input()

# 소켓을 생성 (SOCK_STREAM 은 TCP 소켓을 의미)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 서버에 연결하고 데이터를 전송
    sock.connect((HOST, PORT))
    sock.sendall((data+"\n").encode())

    # 데이터를 수신하고 소켓 연결을 닫음
    received = sock.recv(1024)
finally:
    sock.close()

print ("Sent:     {}".format(data))
print ("Received: {}".format(received))