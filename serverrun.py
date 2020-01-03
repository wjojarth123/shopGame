import socket
import random
import atexit
import threading
import time
from enum import Enum
CustomerState = Enum('CustomerState', 'onStreet goingToShop waiting leavingShop')
class Customer:
	x=-10
	y=205
	budget = 5
	desiredMeal = ['Waffles']
	state = CustomerState.onStreet
	def __init__(self, desiredMeal, budget):
		self.budget=budget
		self.desiredMeal=desiredMeal
		#self.x += random.randrange(-20, 40)

	def __str__(self):
		return str(self.x)+", "+str(self.y)+", "+str(self.budget)+", "+self.desiredMeal

def fromString(str):
	customerlist=str.split(', ')
	customer = Customer('foo', 'bar')
	customer.x=int(customerlist[0])
	customer.y=int(customerlist[1])
	customer.budget=int(customerlist[2])
	customer.desiredMeal=customerlist[3]
	return customer

def generateCustomer(possibleFoods):
	customer = Customer(possibleFoods[random.randrange(0,len(possibleFoods))],random.randrange(2,50))
	#print(customer)

	return customer

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
	messageLength = str(len(message))
	for i in range(4-len(messageLength)):
		messageLength="0"+messageLength

	for player in playerlist:
		player.send(bytes(messageLength,"UTF-8"))
		player.send(bytes(str(message),"UTF-8"))
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
	print('length:', l)
	m=player.recv(l)
	m=m.decode("utf-8")
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
		# print(len(playerlist))
		for i in playerlist:
			print("running2")
			msg=read(i)
			print(msg)
			msg=msg.split(";")
			if msg[0]=="prices":
				prices[int(msg[1])]= eval(msg[2])
				print(prices)
				sendToAll("np;"+msg[1]+";"+msg[2])


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
