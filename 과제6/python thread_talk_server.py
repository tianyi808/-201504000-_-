#팀명 :NB+  과제3 조원 :YAN YIMING (2015040009) CHANG YUXUAN(2015040051)  BI XINYU(2015083061)
#-*- coding:utf-8 -*-
 
import socket
 
#ip/port
ip_port = ('127.0.0.1', 8888)
#소켓 만들기
s = socket.socket()
#고정 ip/port
s.bind(ip_port)
#감청 연결
s.listen()
print('사용자 연결을 기다리는 중... ...')
while(True):
    #연결을 구성한 후 accept을(를) 되돌린 원 그룹을 connect, addr에 부가합니다.
    conn, addr = s.accept()
    if conn is not None:
        print('한 사용자가 .\n에 연결하여 상대방이 메시지를 보내기를 기다리고 있습니다..')
    while(True):
        try:
            recv_data = conn.recv(1024)
            #수신된 메시지 표시
            print('상대방이 보낸 메시지：', str(recv_data, encoding = 'utf-8'))
            send_data = input('답장하겠습니다>>').strip()
            conn.send(bytes(send_data, encoding = 'utf-8'))
            print('상대방이 메시지를 보내기를 기다리다>>')
        except Exception:
            print('원격 호스트가 하나의 기존 연결을 강제로 잠그고, 릴레이가 다른 연결을 기다리도록 했습니다.。')
            break
    conn.close()
