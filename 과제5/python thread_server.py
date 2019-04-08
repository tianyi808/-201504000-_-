#팀명 :NB+  과제3 조원 :YAN YIMING (2015040009) CHANG YUXUAN(2015040051)  BI XINYU(2015083061)
import socket
import threading
import argparse


ADDRESS = ('127.0.0.1', 8888)  # 바인드 주소
 
g_socket_server = None  # 청취 책임이있는 소켓(socket)
 
g_conn_pool = []

def init():
    """
    서버 초기화
    """
    global g_socket_server
    g_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 객체 만들기
    g_socket_server.bind(ADDRESS)
    g_socket_server.listen(5)  # 최대 대기 번호
    print("서버가 시작되어 클라이언트가 연결되기를 기다리고 있습니다....")
def accept_client():
    """
    새로운 연결 받기
    """
    while True:
        client, _ = g_socket_server.accept()  # 차단, 클라이언트 연결 기다림하십시오
        # 연결 풀에 가입하십시오.
        g_conn_pool.append(client)
        # 관리 할 클라이언트마다 별도의 스레드 생성하십시오.
        thread = Thread(target=message_handle, args=(client,))
        # 데몬 스레드로 설정하십시오.
        thread.setDaemon(True)
        thread.start()
 
 
def message_handle(client):
    """
    메시지 처리
    """
    client.sendall("성공적인 서버 연결!".encode(encoding='utf8'))
    while True:
        bytes = client.recv(1024)
        print("클라이언트 메시지:", bytes.decode(encoding='utf8'))
        if len(bytes) == 0:
            client.close()
            # 연결 삭제
            g_conn_pool.remove(client)
            print("오프라인으로 클라이언트가 있습니다.。")
            break
if __name__ == '__main__':
    init()
    # 새 연결을받을 새 스레드
    thread = Thread(target=accept_client)
    thread.setDaemon(True)
    thread.start()
    # 메인 쓰레드 로직
    while True:
        cmd = input("""--------------------------
입력 1 : 현재 줄 번호보기
입력 2 : 지정된 클라이언트에게 메시지 보내기
입력 3 : 서버 닫기
""")
        if cmd == '1':
            print("--------------------------")
            print("현재 온라인 번호：", len(g_conn_pool))
        elif cmd == '2':
            print("--------------------------")
            index, msg = input(""색인, 메시지"형식을 입력하십시오.：").split(",")
            g_conn_pool[int(index)].sendall(msg.encode(encoding='utf8'))
        elif cmd == '3':
            exit()
