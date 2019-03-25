#팀명 :NB+  과제3 조원 :YAN YIMING (2015040009) CHANG YUXUAN(2015040051)  BI XINYU(2015083061)
import socket
 
 
if __name__ == '__main__':
    
    # 프로토콜 만듭니다.
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버와 연결합니다.
    tcp_client_socket.connect(("서버 ip", 8888))

    # 파일 다운로드 요청 보내합니다.
    file_name = input("다운로드 할 파일의 이름을 입력하십시오.：")

    # 개인은 서버 및 클라이언트 측 모두에서 UTF-8 인코딩을 사용합니다.
    file_name_data = file_name.encode("utf-8")

    # 요청 데이터 보내합니다.
    tcp_client_socket.send(file_name_data)

    # 파일에 데이터 씁니다.
    with open("OK,바탕 화면에 저장 됩니다：C:/Users/*/Desktop/" + file_name, "wb") as file:
        while True:

            # 파일 데이터 수신 루프합니다.
            file_data = tcp_client_socket.recv(1024)

            # 데이터 수신 즉시 파일에 씁니다
            if file_data:
                file.write(file_data)
            else:
                print("서버가 데이터를 다 보내고 연결을 닫습니다.")
                break

    # 연결을 닫습니다.
    tcp_client_socket.close()
