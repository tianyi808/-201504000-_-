#팀명 :NB+  과제3 조원 :YAN YIMING (2015040009) CHANG YUXUAN(2015040051)  BI XINYU(2015083061)

import socket
import os
 
 
if __name__ == '__main__':
 
    # os.path의 기본 경로가 변경되어 데스크탑으로 변경되었습니다.
    os.chdir("/home/python/Desktop")
 
    # 프로토콜 만듭니다.
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    # 바인딩 포트 번호, IP 주소가 바인딩되지 않습니다.
    tcp_server_socket.bind(("", 8888))
 
    # 프로그램 종료, 릴리스 포트 번호, 포트 번호 재사용합니다.
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
 
    tcp_server_socket.listen(128)
 
    while True:
        # 새 프로토콜을 만들고 수신 클라이언트의 연결 요청을 기다립니다.
        service_client_socket, ip_port = tcp_server_socket.accept()
        print("클라이언트 연결 성공합니다:", ip_port)
 
        # 고객 요청 정보 수신합니다.
        file_name_data = service_client_socket.recv(1024)
 
        # 이진 데이터 디코딩합니다.
        file_name = file_name_data.decode("utf-8")
 
        # 파일이 존재하는지 확인합니다.
        if os.path.exists(file_name):
            
            # 파일이 존재합니다.
            with open(file_name, "rb") as file:
                # 파일 데이터 읽합니다.
                while True:
                    # 루프는 파일 데이터를 읽합니다.
                    file_data = file.read(1024)
                    #데이터가 읽혔다는 것을 나타냅니다.
                    if file_data:
                        # 클라이언트에 데이터 보냅니다.
                        service_client_socket.send(file_data)
                    else:
                        print("요청 된 파일 데이터가 전송됩니다.")
                        break
 
        else:
            print("다운로드를 요청한 파일이 존재하지 않습니다.")
 
        # 연결을 닫습니다.
        service_client_socket.close()
    # 클라이언트 연결 요청 서비스를 종료합니다. 서버의 프로토콜을 닫을 필요가 없습니다.
    tcp_server_socket.close()

