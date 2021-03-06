{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset134 \'cb\'ce\'cc\'e5;}{\f1\fnil\fcharset129 Malgun Gothic;}}
{\colortbl ;\red0\green0\blue255;}
{\*\generator Riched20 10.0.17763}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang2052 #\f1\'c6\'c0\'b8\'ed\f0\lang1033  :NB+  \par
\lang2052 #\f1\lang1033\'b0\'fa\'c1\'a6\f0  \par
\lang2052 #\f1\lang1033\'c1\'b6\'bf\'f8\f0  :YAN YIMING (2015040009) CHANG YUXUAN(2015040051)  BI XINYU(2015083061)\par
# {{\field{\*\fldinst{HYPERLINK www.baidu.com }}{\fldrslt{www.baidu.com\ul0\cf0}}}}\f0\fs22  \lang2052\'a3\'a8\f1\lang1033\'c1\'df\'b1\'b9\'be\'ee\f0  \f1\'b0\'cb\'bb\'f6\f0  \f1\'bf\'a3\'c1\'f8\f0\lang2052\'a3\'a9\lang1033\par
# CreateDate: 201\lang2052 9\lang1033 -\lang2052 06\lang1033 -\lang2052 08\lang1033\par
\lang2052\par
import socket\par
import io\par
import struct\par
import sys\par
\par
class flushfile(io.FileIO):\par
    def __init__(self, f):\par
        self.f = f\par
    def write(self, x):\par
        self.f.write(x)\par
        self.f.flush()\par
\par
sys.stdout = flushfile(sys.stdout)\par
\par
def main(dest_name):\par
    dest_addr = socket.gethostbyname(dest_name)\par
    port = 30000\par
    max_hops = 30\par
\par
    ttl = 1\par
    while True:\par
        rec_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)\par
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)\par
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)\par
\par
        timeout = struct.pack("ll", 2, 0)\par
        rec_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)\par
\par
        rec_socket.bind(("", port))\par
        sys.stdout.write(" %d   " % ttl)\par
        send_socket.sendto(bytes("", "utf-8"), (dest_name, port))\par
\par
        curr_addr = None\par
        curr_name = None\par
        finished = False\par
        tries = 1\par
        while not finished and tries > 0:\par
            try:\par
                _, curr_addr = rec_socket.recvfrom(512)\par
                finished = True\par
                curr_addr = curr_addr[0]\par
                try:\par
                    curr_name = socket.gethostbyaddr(curr_addr)[0]\par
                except socket.error:\par
                    curr_name = curr_addr\par
            except socket.error as err:\par
                tries -= 1\par
                sys.stdout.write("* ")\par
\par
        send_socket.close()\par
        rec_socket.close()\par
\par
        if not finished:\par
            pass\par
\par
        if curr_addr is not None:\par
            curr_host = "%s (%s)" % (curr_name, curr_addr)\par
        else:\par
            curr_host = ""\par
        sys.stdout.write("%s\\n" % (curr_host))\par
\par
        ttl += 1\par
        if curr_addr == dest_addr or ttl > max_hops:\par
            break\par
\par
if __name__ == "__main__":\par
    main("\lang1033 www.baidu.com\lang2052  ")\par
}
 