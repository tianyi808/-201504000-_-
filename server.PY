#팀명 :NB+  조원 :YAN YIMING (2015040009) CHANG YUXUAN(2015040051)  BI XINYU(2015083061)
# socket 대상을 만든다
import socket

server_receive = socket.socket()
#IP를 확인
ip_port = ("127.0.0.1",8888)
#bind()할당
server_receive.bind(ip_port)
#listen보다
server_receive.listen(5)
#글라이언드가 연결 한다
#accept 요청 링크 수락
conn,addr = server_receive.accept()
while True:
    #데이터를 수락한다
    data = conn.recv(1024)
    if not data:
        break
    else:
        #데이터를 출력한다
        print(str(data,encoding="utf-8"))
    msg = input("대답 해주세요.：").strip()
    if len(data) == 0:
        continue
    conn.sendall(bytes(msg,encoding="utf-8"))
#연결 끊
conn.close()
server_receive.close()
