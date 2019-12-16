import pygame
import time
import random
import client
from enum import Enum
from customersOperations import Customer, generateCustomer,  CustomerState
from traderOperations import *
LOT=[]
mapx=15
mapy=50
startx=-1500
starty=-100
tilemap=[]
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
shopImage=pygame.image.load("buildingTiles_113.png")
bunnyImage=pygame.image.load("buildingTiles_041.png")
roadImage=pygame.image.load("roads.png")
treeImage=pygame.image.load("cityTiles_067.png")
groundImage=pygame.image.load("cityTiles_066.png")
grassImage=pygame.image.load("cityTiles_066.png")
busImage=pygame.image.load("cityTiles_002.png")
Image=pygame.image.load("cityTiles_073.png")
ourImage=pygame.image.load("buildingTiles_100.png")
carImage=pygame.image.load("carBlue2_003.png")
pygame.font.init()
myfont=pygame.font.SysFont('Times New Roman',24)
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
tilemap = client.getTileMap()
tilemap[15+client.AyeDee*2][4]=9
print("iddd", client.AyeDee)
for i in range(0,10,2):
	shopPrice=client.allPlayersPrices[int(i/2)]
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
		client.sendPrices(prices)
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
	if client.updatedPrices:
		for i in range(0,5):
			LOT[i].prices=client.allPlayersPrices[i]
		print("changing pry seas")
		client.updatedPrices=False
	money-=(time.time() - t)/4
	t = time.time()
	drawmapI()
	mousePos=pygame.mouse.get_pos()
	clicked=False
	if checkTiming:
		t2 = time.time()
		print("map drawing took " + str(t2 - t) + 'seconds')

	for event in pygame.event.get():
		if event.type== pygame.KEYDOWN:
			selectedtrader.handleKeypress(event)
		if event.type == pygame.QUIT:
			done = True
		if event.type==pygame.MOUSEBUTTONDOWN:
			clicked=True
			mousePos=pygame.mouse.get_pos()

	if checkTiming:
		t3 = time.time()
		print("Event Handling took " + str(t3 - t2) + 'seconds')

	mouseRect=pygame.Rect(mousePos[0],mousePos[1],1,1)
	for i in range(len(possibleFoods)):
		buyrect = pygame.Rect(700,i*35,50,50)
		if mouseRect.colliderect(buyrect) and clicked and money> selectedtrader.prices[possibleFoods[i]]:
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
	customers += client.newCustomers
	client.newCustomers=[]
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
