import pygame
import time
import random
from enum import Enum
from customersOperations import Customer, generateCustomer,  CustomerState
from traderOperations import *
LOT=[]
selectedtrader=0
pygame.init()
buyrect=pygame.Rect(650,60,80,30)
screen = pygame.display.set_mode((800, 600))
mealList=['Bread', 'Potatoes', 'Waffles','Spaghetti','Soup','Pizza','Ice cream','Sushi','Chicken','Roast Beef']
possibleFoods = ['Bread', 'Potatoes', 'Waffles','Spaghetti','Soup','Pizza','Ice cream','Sushi','Chicken','Roast Beef']
Done=False
readyToServe = False
timeLastServed=time.time()
servingSpeed=1
money=100

pygame.font.init()
myfont=pygame.font.SysFont('Times New Roman',24)
stock =	{
  "Potatoes": 5,
  "Bread": 6,
  'Waffles':0,
  'Spaghetti': 0,
  'Soup': 0,
  'Pizza': 0,
  'Ice cream': 0,
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
  'Ice cream':0,
  'Sushi':0,
  'Chicken':0,
  'Roast Beef':0
}
rationalPrices =	{
  "Potatoes": 5,
  "Bread": 5,
  'Waffles':10,
  'Spaghetti':10,
  'Soup':5,
  'Pizza':10,
  'Ice cream':5,
  'Sushi':5,
  'Chicken':10,
  'Roast Beef':10
}
#sustomerState = Enum('CustomerState', 'onStreet goingToShop waiting leavingShop')


customers = []

def drawSlider(food, mousePos, clickedOn):
	rect=pygame.Rect(5,(possibleFoods.index(food)+1)*25+160,150,10)
	textsurface=myfont.render(food+" , "+str(prices[food]),False,(255,255,255))
	screen.blit(textsurface,(50,(possibleFoods.index(food)+1)*25+170))
	pygame.draw.rect(screen,(255,255,255),rect)
	if rect.contains(pygame.Rect(mousePos[0], mousePos[1], 1, 1)) and clickedOn:
		newPrice = int((mousePos[0]-5)/3)

		prices[food]=newPrice
	sliderect=pygame.Rect((prices[food]*3)-10,((possibleFoods.index(food)+1)*25)+155,20,20)
	pygame.draw.rect(screen,(0, 150, 50),sliderect)

def moveCustomers():
	#print("attempting to move",)
	global money
	global timeLastServed
	for c in customers:
		if c.state == CustomerState.onStreet:
			c.y += 5
		elif c.state == CustomerState.goingToShop:
			c.x += 5
		elif c.state==CustomerState.waiting:
			#print(time.time()-timeLastServed)
			if time.time()-timeLastServed>=servingSpeed:
				timeLastServed=time.time()
				c.state=CustomerState.leavingShop
				if stock[c.desiredMeal] >0 and c.budget>prices[c.desiredMeal] :
					amountOverpriced = (prices[c.desiredMeal]-rationalPrices[c.desiredMeal])*2.5
					if random.randrange(0,100)>amountOverpriced:
						money+=prices[c.desiredMeal]
						stock[c.desiredMeal] -= 1
		if c.state == CustomerState.leavingShop:
			c.y += 5
#or i in customers:
	#print(i)
customerSpawnTime=time.time()
for i in range(0,5):
	LOT.append(generateTrader(200,i*100, possibleFoods))
selectedtrader=LOT[0]
while not Done:
	money-=0.1
	screen.fill((0,0,0))
	mousePos=pygame.mouse.get_pos()
	clicked=False
	for event in pygame.event.get():
		if event.type== pygame.KEYDOWN:
			selectedtrader.handleKeypress(event)
		if event.type == pygame.QUIT:
			done = True
		if event.type==pygame.MOUSEBUTTONDOWN:
			clicked=True
			mousePos=pygame.mouse.get_pos()
	mouseRect=pygame.Rect(mousePos[0],mousePos[1],1,1)
	if buyrect.contains(mouseRect) and clicked and money> selectedtrader.prices[selectedtrader.item]:
		stock[selectedtrader.item] += 1
		print("buy"+selectedtrader.item)
		money-=selectedtrader.prices[selectedtrader.item]
	for i in range(len(LOT)):
		traderrect=pygame.Rect(LOT[i].x,LOT[i].y,100,50)
		if traderrect.contains(pygame.Rect(mousePos[0], mousePos[1], 1, 1)) and clicked:
			selectedtrader=LOT[i]

	trade(selectedtrader,screen)
	for meal in mealList:
		drawSlider(meal,mousePos,clicked)
	rect = pygame.Rect(320,0,120,600)
	pygame.draw.rect(screen, (200, 200, 200), rect)
	if time.time()-customerSpawnTime>=0.1:
		customers.append(generateCustomer(possibleFoods))
		customerSpawnTime=time.time()
	shoprect = pygame.Rect(550,150,200,300)
	pygame.draw.rect(screen, (0, 150, 50), shoprect)
	moveCustomers()
	for trader in LOT:
		traderRect=pygame.Rect(trader.x,trader.y,100,50)
		pygame.draw.rect(screen,(100,0,0),traderRect)
	for i in customers:
		if i.y==360 and i.desiredMeal in mealList and i.state == CustomerState.onStreet and i.budget>=prices[i.desiredMeal] and stock[i.desiredMeal]>0 and prices[i.desiredMeal]:
			amountOverpriced = (prices[i.desiredMeal]-rationalPrices[i.desiredMeal])*2.5
			if random.randrange(0,100)>amountOverpriced:
				#print("yay! a customer entered with the meal of: " + i.desiredMeal)
				i.state = CustomerState.goingToShop
		if i.x>=600 and i.state==CustomerState.goingToShop:
			i.state = CustomerState.waiting

		rect = pygame.Rect(i.x,i.y,10,10)
		pygame.draw.rect(screen, (0, 0,255 -  possibleFoods.index(i.desiredMeal)*(255/len(possibleFoods))), rect)
	# print("")
	textsurface=myfont.render("Money: "+str(money),False,(255,255,255))
	screen.blit(textsurface,(5,5))
	for i in range(len(mealList)):
		textsurface=myfont.render(mealList[i]+str(stock[mealList[i]]),False,(255,255,255))
		screen.blit(textsurface,(5,(i+1)*15))
		pygame.display.flip()
