import socket
import random
import atexit
import threading
playerlist=[]
tilemap = []
mapx=15
mapy=50
'''
=======================================
=======================================
make tilemap
=======================================
=======================================
'''
def makeTileMap():
	for i in range(mapy):
		list=[]
		for o in range(mapx):
			if o==5:
				list.append(random.randint(0,1))
			else:
				list.append(random.randint(2,4))
		tilemap.append(list)
	for i in range(0,5*2, 2):
		tilemap[12+i][6]=5
		tilemap[12+i+1][6]=4
		tilemap[12+i+1][5]=6
	tilemap[20][4]=7
makeTileMap()
'''
=======================================
=======================================
started socket
=======================================
=======================================
'''
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port=12344 
s.bind(('',port))
s.listen(5)

def end():
	print("Closing Socket")
	for player in playerlist:
		player.send(bytes("closed","UTF-8"))
	s.close()

atexit.register(end)

def sendToAll(message):
	messageLength = str(len(message))
	for i in range(4-len(messageLength)):
		messageLength="0"+messageLength

	for player in playerlist:
		player.send(bytes(messageLength,"UTF-8"))
		player.send(bytes(str(message),"UTF-8"))
def listen():
	while True:
		client, address = s.accept()
		playerlist.append(client)
t1=threading.Thread(target=listen)
t1.start()

while len(playerlist) < 2:
	pass

sendToAll(str(tilemap))

while len(playerlist) >= 2:
	message="foo"
	sendToAll("hi")
print('ready')
