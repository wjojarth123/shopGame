import random
import pygame
import sys
import os

if getattr(sys, 'frozen', False):
	Path = sys._MEIPASS  # This is for when the program is frozen
else:
	Path = os.path.dirname(__file__)  # This is when the program normally runs

shopImage = pygame.image.load(os.path.join(Path, "buildingTiles_113.png"))


breadImage=pygame.image.load(os.path.join(Path, "bread.png"))
potatoImage=pygame.image.load(os.path.join(Path, "potato.png"))
wafflesImage=pygame.image.load(os.path.join(Path, "waffles.png"))
chickenImage=pygame.image.load(os.path.join(Path, "chicken.png"))
soupImage=pygame.image.load(os.path.join(Path, "soup.png"))
roastImage=pygame.image.load(os.path.join(Path, "roastbeef.png"))
sushiImage=pygame.image.load(os.path.join(Path, "sushi.png"))
iceCreamImage=pygame.image.load(os.path.join(Path, "iceCream.png"))
spaghettiImage=pygame.image.load(os.path.join(Path, "Spaghetti.png"))
pizzaImage=pygame.image.load(os.path.join(Path, "pizza.png"))
adImage=pygame.image.load(os.path.join(Path, "ad.png"))

buyImage=pygame.image.load(os.path.join(Path, "buy.png"))
pygame.font.init()
all_fonts=pygame.font.get_fonts()
myfont=pygame.font.SysFont(all_fonts[0],24)
class Trader:
	item='Bread'
	x=360
	y=0
	rect=0
	prices =	{
	 'Bread':5,
	 'Potatoes':5,
	 'Waffles': 5,
	 'Spaghetti': 5,
	 'Soup': 5,
	 'Pizza': 5,
	 'Ice cream': 5,
	 'Sushi': 5,
	 'Chicken': 5,
	 'Roast beef': 5,
	 'Ad':50
	}
	def __init__(self, prices,x,y, rect):
		self.prices = prices
		self.x = x
		self.y = y
		self.rect=rect



text=''
def makeitem(image,y,trader,item,screen):
	print(trader.prices)
	screen.blit(image,(610,y))
	screen.blit(buyImage,(700,y-10))
	textsurface=myfont.render(str(trader.prices[item]),False,(0,0,0))
	screen.blit(textsurface,(650,y))
def generateTrader(x, y, possibleFoods, rect,run,p=None):
	traderPrices = {}
	if run or p==0:
		for food in possibleFoods:
			traderPrices[food] = random.randrange(11,30)
	else:
		traderPrices = p

	traderPrices['Ad'] = 50
	trader = Trader(traderPrices,x,y,rect)
	return trader
def trade(trader, screen):
	print(trader.prices)
	windowrect=pygame.Rect(600,0,200,430)
	pygame.draw.rect(screen,(255,255,255),windowrect)
	offset = 37

	makeitem(breadImage,10,trader,"Bread",screen)
	makeitem(potatoImage,10 + offset*1,trader,"Potatoes",screen)
	makeitem(wafflesImage,10 + offset*2,trader,"Waffles",screen)
	makeitem(spaghettiImage,10 + offset*3,trader,"Spaghetti",screen)
	makeitem(soupImage,10 + offset*4,trader,"Soup",screen)
	makeitem(pizzaImage,10 + offset*5,trader,"Pizza",screen)
	makeitem(iceCreamImage,10 + offset*6,trader,"Ice Cream",screen)
	makeitem(sushiImage,10 + offset*7,trader,"Sushi",screen)
	makeitem(chickenImage,10 + offset*8,trader,"Chicken",screen)
	makeitem(roastImage,10 + offset*9,trader,"Roast Beef",screen)



	if "Ad" in trader.prices:
		makeitem(adImage,10 + offset*10,trader,"Ad",screen)

priceOfitem=0
import random
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
"""=================================
====================================
===============client===============
====================================
===================================="""
import socket
import atexit
import threading
import time
def end():
	s.close()
atexit.register(end)
#IP="127.0.0.1"
IP="73.241.173.145"
s=socket.socket()
port=12344
s.connect((IP,port))
AyeDee=0
tilemap = []
allPlayersPrices=[{"Potatoes": 5,
  "Bread": 5,
  'Waffles':10,
  'Spaghetti':10,
  'Soup':5,
  'Pizza':10,
  'Ice Cream':5,
  'Sushi':5,
  'Chicken':10,
  'Roast Beef':10},{  "Potatoes": 5,
	"Bread": 5,
	'Waffles':10,
	'Spaghetti':10,
	'Soup':5,
	'Pizza':10,
	'Ice Cream':5,
	'Sushi':5,
	'Chicken':10,
	'Roast Beef':10},{ "Potatoes": 5,
	  "Bread": 5,
	  'Waffles':10,
	  'Spaghetti':10,
	  'Soup':5,
	  'Pizza':10,
	  'Ice Cream':5,
	  'Sushi':5,
	  'Chicken':10,
	  'Roast Beef':10},{"Potatoes": 5,
		"Bread": 5,
		'Waffles':10,
		'Spaghetti':10,
		'Soup':5,
		'Pizza':10,
		'Ice Cream':5,
		'Sushi':5,
		'Chicken':10,
		'Roast Beef':10},{"Potatoes": 5,
		  "Bread": 5,
		  'Waffles':10,
		  'Spaghetti':10,
		  'Soup':5,
		  'Pizza':10,
		  'Ice Cream':5,
		  'Sushi':5,
		  'Chicken':10,
		  'Roast Beef':10}]
updatedPrices = False
newCustomers = []
def read():
	l=int(s.recv(4))
	m=s.recv(l)
	m=m.decode("utf-8")
	while not len(m) == l :
		v=s.recv(l-len(m))
		v=v.decode("utf-8")
		m+=v

	return m
tilemap=eval(read())
def getTileMap():
	return tilemap

def getNewCustomers():
	return newCustomers
def sendPrices(prices):
	send("prices;"+str(AyeDee)+";"+str(prices))

def send(message):
	message=str(message)
	messageLength = str(len(message))
	for i in range(4-len(messageLength)):
		messageLength="0"+messageLength

	print(messageLength)
	print(len(message))
	print(message)
	s.send(bytes(messageLength,"UTF-8") + bytes(message,"UTF-8"))
def listen():
	global AyeDee
	global updatedPrices
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
			print("switch prices")
			m=m.split(";")
			allPlayersPrices[int(m[1])+1]=eval(m[2])
			updatedPrices=True
		print(m)
def sendx():
	while True:
		time.sleep(1)
		#send("foo")
t1=threading.Thread(target=listen)
t1.start()
t2=threading.Thread(target=sendx)
t2.start()


import pygame
import random
import sys
import os
from enum import Enum
LOT=[]
mapx=15
mapy=50
startx=-1500
starty=-100
# tilemap=[]
selectedtrader=0
pygame.init()
screen = pygame.display.set_mode((800, 600))
mealList=['Bread', 'Potatoes', 'Waffles','Spaghetti','Soup','Pizza','Ice Cream','Sushi','Chicken','Roast Beef']
possibleFoods = mealList
Done=False
readyToServe = False
timeLastServed=time.time()
servingSpeed=1
money=100
shopImage=pygame.image.load(os.path.join(Path, "buildingTiles_113.png"))
bunnyImage=pygame.image.load(os.path.join(Path, "buildingTiles_041.png"))
roadImage=pygame.image.load(os.path.join(Path, "roads.png"))
treeImage=pygame.image.load(os.path.join(Path, "cityTiles_067.png"))
groundImage=pygame.image.load(os.path.join(Path, "cityTiles_066.png"))
grassImage=pygame.image.load(os.path.join(Path, "cityTiles_066.png"))
busImage=pygame.image.load(os.path.join(Path, "cityTiles_002.png"))
Image=pygame.image.load(os.path.join(Path, "cityTiles_073.png"))
ourImage=pygame.image.load(os.path.join(Path, "buildingTiles_100.png"))
carImage=pygame.image.load(os.path.join(Path, "carBlue2_003.png"))
pygame.font.init()
all_fonts=pygame.font.get_fonts()
myfont=pygame.font.SysFont(all_fonts[0],16)
t=time.time()
imageList=[busImage,roadImage,grassImage,groundImage,treeImage,shopImage,Image,ourImage,carImage,bunnyImage]
stock =	{
  "Potatoes": 5,
  "Bread": 6,
  'Waffles':0,
  'Spaghetti': 0,
  'Soup': 0,
  'Pizza': 0,
  'Ice Cream': 0,
  'Sushi': 0,
  'Chicken': 0,
  'Roast Beef': 0
}
prices =	{
  "Potatoes": 3,
  "Bread": 5,
  'Waffles':0,
  'Spaghetti':0,
  'Soup':0,
  'Pizza':0,
  'Ice Cream':0,
  'Sushi':0,
  'Chicken':0,
  'Roast Beef':0
}
amountOfads=0
rationalPrices =	{
  "Potatoes": 5,
  "Bread": 5,
  'Waffles':10,
  'Spaghetti':10,
  'Soup':5,
  'Pizza':10,
  'Ice Cream':5,
  'Sushi':5,
  'Chicken':10,
  'Roast Beef':10
}
#sustomerState = Enum('CustomerState', 'onStreet goingToShop waiting leavingShop')


customers = []


# makeTileMap()
tilemap = getTileMap()
print(tilemap)
tilemap[15+AyeDee*2][4]=9
print("iddd", AyeDee)
for i in range(0,10,2):
	shopPrice=allPlayersPrices[int(i/2)]
	LOT.append(generateTrader(200,i*100, possibleFoods,pygame.Rect(4*132+(12+i+1)*66+startx,(12+i+1)*33+starty-imageList[tilemap[12+i+1][4]].get_rect().size[1],132,127),False,shopPrice))
	print(shopPrice)
	print("jj")
	print(4*132+(12+i+1)*66+startx,(12+i+1)*33+starty-imageList[tilemap[12+i+1][4]].get_rect().size[1])

#tilemap[12+i+1][4]
for i in range(0, 10, 2):

	LOT.append(generateTrader(200,i*100, possibleFoods,pygame.Rect(6*132+(12+i)*66+startx,(12+i)*33+starty-imageList[tilemap[12+i][6]].get_rect().size[1],132,127),True))

print(tilemap)
def drawSlider(food, mousePos, clickedOn):
	rect=pygame.Rect(5,(possibleFoods.index(food)+1)*25+160,150,10)
	textsurface=myfont.render(food+" , "+str(prices[food]),False,(255,255,255))
	screen.blit(textsurface,(50,(possibleFoods.index(food)+1)*25+170))
	pygame.draw.rect(screen,(255,255,255),rect)
	if rect.contains(pygame.Rect(mousePos[0], mousePos[1], 1, 1)) and clickedOn:
		newPrice = int((mousePos[0]-5)/3)
		prices[food]=newPrice
		sendPrices(prices)
		print("11111")
	sliderect=pygame.Rect((prices[food]*3)-10,((possibleFoods.index(food)+1)*25)+155,20,20)
	pygame.draw.rect(screen,(0, 150, 50),sliderect)
'''
=======================================
=======================================
draw map
=======================================
=======================================
'''
def drawmapI():
	for i in range(mapy):
		for o in range(mapx):
			screen.blit(imageList[tilemap[i][o]],(o*132+i*66+startx,i*33+starty-imageList[tilemap[i][o]].get_rect().size[1]))

def moveCustomers():
	#print("attempting to move",)
	global money
	global timeLastServed
	for c in customers:
		if c.state == CustomerState.onStreet:
			c.y += 2.5
			c.x += 5
		elif c.state == CustomerState.goingToShop:
			c.x += 5
			c.y += 2.5
		elif c.state==CustomerState.waiting:
			#print(time.time()-timeLastServed)
			if time.time()-timeLastServed>=servingSpeed:
				timeLastServed=time.time()
				c.state=CustomerState.leavingShop
				if stock[c.desiredMeal] >0 and c.budget>prices[c.desiredMeal] :
					amountOverpriced = (prices[c.desiredMeal]-rationalPrices[c.desiredMeal])*2.5
					if random.randrange(0,100 + amountOfads)>amountOverpriced:
						money+=prices[c.desiredMeal]
						stock[c.desiredMeal] -= 1
		if c.state == CustomerState.leavingShop:
			c.y += 2.5
			c.x += 5
#or i in customers:
	#print(i)
# customerSpawnTime=time.time()

selectedtrader=LOT[0]

checkTiming = False

'''
=======================================
=======================================
while loop
=======================================
=======================================
'''

drawmapI()
while not Done:
	if updatedPrices:
		for i in range(0,5):
			LOT[i].prices=allPlayersPrices[i]
			print(allPlayersPrices[i])
		print("changing pry seas")
		updatedPrices=False
	money-=(time.time() - t)/4
	t = time.time()
	drawmapI()
	mousePos=pygame.mouse.get_pos()
	clicked=False
	if checkTiming:
		t2 = time.time()
		print("map drawing took " + str(t2 - t) + 'seconds')

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			pygame.display.update
			pygame.quit()
			exit()
			sysExit(0)
			Exit()
			os.kill(os.getppid(), signal.SIGHUP)
		if event.type==pygame.MOUSEBUTTONDOWN:
			clicked=True
			mousePos=pygame.mouse.get_pos()

	if checkTiming:
		t3 = time.time()
		print("Event Handling took " + str(t3 - t2) + 'seconds')

	mouseRect=pygame.Rect(mousePos[0],mousePos[1],1,1)
	for i in range(len(possibleFoods)):
		buyrect = pygame.Rect(700,i*37,50,50)
		if mouseRect.colliderect(buyrect) and clicked and money> selectedtrader.prices[possibleFoods[i]] and selectedtrader.prices[possibleFoods[i]]>10:
			if not selectedtrader.item=='Ad':
				stock[possibleFoods[i]] += 1
				print("buy"+selectedtrader.item)
				money-=selectedtrader.prices[possibleFoods[i]]
			else:
				amountOfads+=20
				money-=selectedtrader.prices[selectedtrader.item]
	for i in range(len(LOT)):
		if LOT[i].rect.contains(pygame.Rect(mousePos[0], mousePos[1], 1, 1)) and clicked:
			selectedtrader=LOT[i]

	trade(selectedtrader,screen)
	if checkTiming:
		t4=time.time()
		print("trader Handling took " + str(t4 - t3) + 'seconds')




	'''if time.time()-customerSpawnTime>=random.randint(1,3):
		customers.append(generateCustomer(possibleFoods))
		customerSpawnTime=time.time()'''
	customers += newCustomers
	newCustomers=[]
	moveCustomers()
	for i in customers:
		if i.y==360 and i.desiredMeal in mealList and i.state == CustomerState.onStreet and i.budget>=prices[i.desiredMeal] and stock[i.desiredMeal]>0 and prices[i.desiredMeal]:
			amountOverpriced = (prices[i.desiredMeal]-rationalPrices[i.desiredMeal])*2.5
			if random.randrange(0,100)>amountOverpriced:
				#print("yay! a customer entered with the meal of: " + i.desiredMeal)
				i.state = CustomerState.goingToShop
		if i.x>=600 and i.state==CustomerState.goingToShop:
			print("h")
			i.state = CustomerState.waiting
		screen.blit(carImage,(i.x,i.y))
	if checkTiming:
		t5=time.time()
		print("trader Handling took " + str(t5 - t4) + 'seconds')
		#rect = pygame.Rect(i.x,i.y,10,10)
		#pygame.draw.rect(screen, (0, 0,255 -  possibleFoods.index(i.desiredMeal)*(255/len(possibleFoods))), rect)
	# print("")
	print(selectedtrader.prices)
	for meal in mealList:
		drawSlider(meal,mousePos,clicked)
	textsurface=myfont.render("Money: "+str(round(money, 2)),False,(255,255,255))
	screen.blit(textsurface,(5,5))
	for i in range(len(mealList)):
		textsurface=myfont.render(mealList[i]+str(stock[mealList[i]]),False,(255,255,255))
		screen.blit(textsurface,(5,(i+1)*15))
	textsurface=myfont.render('Amount of ads:'+str(amountOfads),False,(255,255,255))
	screen.blit(textsurface,(5,165))
	pygame.display.flip()
	if money<=0:
		print("you  loser, you just lost again!!!!!")
		Done=True
	if checkTiming:
		t6=time.time()
		print("Meal Handling took " + str(t6 - t5) + 'seconds')



		print("One loop took " + str( time.time() - t) + 'seconds')
print("goodby")
pygame.display.quit()
pygame.quit()
exit()
