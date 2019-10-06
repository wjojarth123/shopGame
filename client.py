import socket
import atexit
import threading
from customersOperations import Customer,fromString
def end():
    s.close()
atexit.register(end)
IP="127.0.0.1"
s=socket.socket()
port=12344
s.connect((IP,port))

tilemap = []

newCustomers = []
def read():
    l=int(s.recv(4))
    m=s.recv(l)
    m=m.decode("utf-8")
    return m
tilemap=eval(read())
def listen():
    while True:
        m=read()
        if m.startswith("customers"):
            m = m[9:]
            print(m)
            newCustomers.append(fromString(m))
        print(m)
t1=threading.Thread(target=listen)
t1.start()
def getTileMap():
    return tilemap

def getNewCustomers():
    return newCustomers
