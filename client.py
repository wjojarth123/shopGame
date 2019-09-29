import socket
import atexit
import threading
def end():
    s.close()
atexit.register(end)
IP="127.0.0.1"
s=socket.socket()
port=12344
s.connect((IP,port))

tilemap = []

def read():
    l=int(s.recv(4))
    m=s.recv(l)
    m=m.decode("utf-8")
    return m

tilemap=eval(read())
def tt():
    while True:
        m=read()
        print(m)
t1=threading.Thread(target=tt)
t1.start()
def getTileMap():
    return tilemap
