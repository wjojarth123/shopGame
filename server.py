import socket
import random
import atexit
import threading
import time
from customersOperations import Customer, generateCustomer,  CustomerState
playerlist=[]
tilemap = []
mapx=15
mapy=50
prices=[0,0,0,0,0]
mealList=['Bread', 'Potatoes', 'Waffles','Spaghetti','Soup','Pizza','Ice Cream','Sushi','Chicken','Roast Beef']
possibleFoods = mealList
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
		tilemap[12+i+1][4]=7
makeTileMap()
print(len(tilemap))
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
def sendToAll(message):
	for player in playerlist:
		try:
			send(player,message)
		except:
			pass
def send(player,message):
	message=str(message)
	messageLength = str(len(message))
	for i in range(4-len(messageLength)):
		messageLength="0"+messageLength

	print(messageLength)
	print(len(message))
	player.send(bytes(messageLength,"UTF-8"))
	player.send(bytes(str(message),"UTF-8"))
def end():
	print("Closing Socket")
	sendToAll("close")
	s.close()
def read(player):
	l=int(player.recv(4))
	m=player.recv(l)
	m=m.decode("utf-8")
	while not len(m) == l :
		v=player.recv(l-len(m))
		v=v.decode("utf-8")
		m+=v
	return m
atexit.register(end)
customerSpawnTime=time.time()

def listen():
	while True:
		print('listening')
		client, address = s.accept()
		send(client,tilemap)
		send(client,"playerID"+str(len(playerlist)))
		print("playerID"+str(len(playerlist)))
		playerlist.append(client)
		print('get out of here, new guy')
def listenForPrices():
	while True:
		print(len(playerlist))
		for i in playerlist:
			try:
				print("running2")
				msg=read(i)
				print(msg)
				msg=msg.split(";")
				if msg[0]=="prices":
					prices[int(msg[1])]= eval(msg[2])
					print(prices)
					sendToAll("np;"+msg[1]+";"+msg[2])
			except:
				print("Networking error!")
				pass


t1=threading.Thread(target=listen)
t1.start()
t2=threading.Thread(target=listenForPrices)
t2.start()


while len(playerlist) < 2:
	pass

sendToAll(str(tilemap))

while len(playerlist) >= 2:
	# print(prices)l
	if time.time()-customerSpawnTime>=random.randint(1,3):
		sendToAll("customers"+str(generateCustomer(possibleFoods)))
		customerSpawnTime=time.time()
print('ready')
