#팀명 :NB+  조원 :YAN YIMING (2015040009) CHANG YUXUAN(2015040051)  BI XINYU(2015083061)
#socket대상을 만든다
import socket

client_send = socket.socket()

#IP를 확인
ip_port = ("127.0.01",8888)
#글라이언드가 연결 한다
client_send.connect(ip_port)

while True:
    #메시지를 보낸다
    msg = input("입력하세요：")
    if len(msg) == 0:
        continue
    elif msg == "exit":
        break
    client_send.sendall(bytes(msg,encoding="utf-8"))
    #메시지를 반다
    data = client_send.recv(1024)
    print(str(data,encoding="utf-8"))

#연결 끊
client_send.close()

