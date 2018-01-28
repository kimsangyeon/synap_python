import select
import socket


ip = '127.0.0.1'
port = 55555
size = 1024

# 소켓생성
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 바인드
server.bind((ip, port))
# 리슨, 여기까지는 기본적인 서버 소켓 세팅
server.listen()
# select 함수에서 관찰될 소켓 리스트 설정
input_list = [server]

while True:
    # select 함수는 관찰될 read, write, except 리스트가 인수로 들어가며
    # 응답받은 read, write, except 리스트가 반환된다.
    # input_list 내에 있는 소켓들에 데이터가 들어오는지 감시한다.
    # 다르게 말하면 input_list 내에 읽을 준비가 된 소켓이 있는지 감시한다.
    input_ready, write_ready, except_ready = select.select(input_list, [], [],30)

    # 응답받은 read 리스트 처리
    for ir in input_ready:
        # 클라이언트가 접속했으면 처리함
        if ir == server:
            client, address = server.accept()
            print(address, 'is connected', flush=True)
            # input_list에 추가함으로써 데이터가 들어오는 것을 감시함
            input_list.append(client)

        # 클라이언트소켓에 데이터가 들어왔으면
        else:
            data = ir.recv(size)
            if data:
                print(ir.getpeername(), 'send :', data, flush=True)
                ir.send(data)
            # 데이터가 없는경우, 즉 클라이언트에서 소켓을 close 한경우
            else:
                print(ir.getpeername(), 'close', flush=True)
                ir.close()
                # 리스트에서 제거
                input_list.remove(ir)

server.close()