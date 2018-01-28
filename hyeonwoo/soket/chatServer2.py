import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        """
        클라이언트와 연결될 때 호출되는 함수
        상위 클래스에는 handle() 메서드가 정의되어 있지 않기 때문에
        여기서 오버라이딩을 해야함
        """
        self.data = self.request.recv(1024).strip()
        print ("{} wrote:".format(self.client_address[0]),)
        print (self.data)
        # 영어의 소문자 데이터를 receive 하면 대문자로 변환해 send
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 3001

    # 서버를 생성합니다. 호스트는 localhost, 포트 번호는 3000
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    print("waiting for connection...")

    # Ctrl - C 로 종료하기 전까지는 서버는 멈추지 않고 작동
    server.serve_forever()