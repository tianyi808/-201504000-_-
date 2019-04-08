#팀명 :NB+  과제3 조원 :YAN YIMING (2015040009) CHANG YUXUAN(2015040051)  BI XINYU(2015083061)
import sys
import socket
import argparse
 
def test_client(host, 8888):
    
    # TCP 소켓 만들기
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 연결 서버
    srv_addr = (host, 8888)
    sock.connect(srv_addr)
    
    # 데이터 송수신
    try:
        # 메시지 보내기
        while True:          
            msg = raw_input("Please nput:")
            sock.sendall(msg)
            
            if msg=="quit" or msg=="exit":
                break            
            
            # 메시지 수신
            data = sock.recv(1024)
            print "Message from server: %s" % data
        sock.close()
    except socket.errno, e:
        print "Socket error: %s" % str(e)
    except Exception as e:
        print "Other exception: %s" % str(e)
    finally:
        sock.close()
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket Server Example")
    parser.add_argument("--ip", action="store", dest="host", type=str, required=True)
    parser.add_argument("--port", action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    test_client(host, port)  

input("")
