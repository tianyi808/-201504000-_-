#팀명 :NB+  과제3 조원 :YAN YIMING (2015040009) CHANG YUXUAN(2015040051)  BI XINYU(2015083061)

#-*- coding:utf-8 -*-
 
import socket
 
#호스트에 연결할 ip/port가 구성될 때까지 대기
ip_port = ('127.0.0.1', 8888)
#소켓 만들기
s = socket.socket()
#연결을 만들다
s.connect(ip_port)
while(True):
    #메시지를 보내
    send_data = input('상대방에게 메시지를 보내다：').strip()
    s.send(bytes(send_data, encoding = 'utf-8'))
    print('상대방의 회답을 기다리다:')
    #메시지를 수신하고 표시
    recv_data = s.recv(1024)
    print('너는 새로운 소식이 있다.:', str(recv_data, encoding = 'utf-8'))
s.close()
