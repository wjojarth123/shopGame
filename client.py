import socket
import atexit
import threading
import time
from customersOperations import Customer,fromString
def end():
    s.close()
atexit.register(end)
IP="127.0.0.1"
s=socket.socket()
port=12344
s.connect((IP,port))
AyeDee=0
tilemap = []
allPlayersPrices=[0,0,0,0,0]
newCustomers = []
def read():
    l=int(s.recv(4))
    m=s.recv(l)
    m=m.decode("utf-8")
    return m
tilemap=eval(read())
def send(message):
	message=str(message)
	messageLength = str(len(message))
	for i in range(4-len(messageLength)):
		messageLength="0"+messageLength

	print(messageLength)
	print(len(message))
	s.send(bytes(messageLength,"UTF-8") + bytes(str(message),"UTF-8"))
def listen():
    global AyeDee
    while True:
        m=read()
        if m.startswith("customers"):
            m = m[9:]
            print(m)
            newCustomers.append(fromString(m))
        elif m.startswith("playerID"):
            m = int(m[8:])
            print("recieved id: ", m)
            AyeDee=m
        elif m.startswith("np"):
            m=m.split(";")
            allPlayersPrices[m[1]]=m[2]
        print(m)
def sendx():
    while True:
        time.sleep(1)
        send("foo")
t1=threading.Thread(target=listen)
t1.start()
t2=threading.Thread(target=sendx)
t2.start()


def getTileMap():
    return tilemap

def getNewCustomers():
    return newCustomers
def sendPrices(prices):
    send("prices;"+str(AyeDee)+";"+str(prices))
