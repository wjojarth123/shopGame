import socket
import atexit
def end():
    s.close()
atexit.register(end)
IP="127.0.0.1"
s=socket.socket()
port=12345
s.connect((IP,port))

def read():
    l=int(s.recv(4))
    m=s.recv(l)
    m=m.decode("utf-8")
    return m

while True:
    m=read()
    print(m)
