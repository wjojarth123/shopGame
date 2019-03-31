import pygame
import time
import random
from enum import Enum
pygame.init()
screen = pygame.display.set_mode((800, 600))
mealList=['Bread','Potatoes']
possibleFoods = ['Bread', 'Potatoes', 'Waffles']
Done=False
readyToServe = False
timeLastServed=time.time()
servingSpeed=5
money=0
pygame.font.init()
myfont=pygame.font.SysFont('Times New Roman',24)
stock =	{
  "Potatoes": 5,
  "Bread": 6
}
prices =	{
  "Potatoes": 3,
  "Bread": 5
}
CustomerState = Enum('CustomerState', 'onStreet goingToShop waiting leavingShop')

class Customer:
	x=360
	y=0
	budget = 5
	desiredMeal = ['Waffles']
	state = CustomerState.onStreet
	def __init__(self, desiredMeal, budget):
		self.budget=budget
		self.desiredMeal=desiredMeal

	def __str__(self):
		return str(self.x)+", "+str(self.y)+", "+str(self.budget)+", "+self.desiredMeal

customers = []

def moveCustomers():
	global money
	global timeLastServed
	for c in customers:
		if c.state == CustomerState.onStreet:
			c.y += 1
		elif c.state == CustomerState.goingToShop:
			c.x += 1
		elif c.state==CustomerState.waiting:
			print(time.time()-timeLastServed)
			if time.time()-timeLastServed>=servingSpeed :
				timeLastServed=time.time()
				c.state=CustomerState.leavingShop
				money+=prices[c.desiredMeal]
		if c.state == CustomerState.leavingShop:
			c.y += 1
def generateCustomer():
	customer = Customer(possibleFoods[random.randrange(0,len(possibleFoods))],random.randrange(2,20))
	customers.append(customer)
	return customer
generateCustomer()
for i in customers:
	print(i)
customerSpawnTime=time.time()
while not Done:
	screen.fill((0,0,0))
	rect = pygame.Rect(320,0,120,600)
	pygame.draw.rect(screen, (200, 200, 200), rect)
	if time.time()-customerSpawnTime>=3:
		generateCustomer()
		customerSpawnTime=time.time()
	rect = pygame.Rect(550,150,200,300)
	pygame.draw.rect(screen, (0, 150, 50), rect)
	moveCustomers()
	for i in customers:
		if i.y==360 and i.desiredMeal in mealList and i.state == CustomerState.onStreet and i.budget>=prices[i.desiredMeal]:
			print("yay! a customer entered with the meal of: " + i.desiredMeal)
			i.state = CustomerState.goingToShop
		if i.x==600 and i.state==CustomerState.goingToShop:
			i.state = CustomerState.waiting
		


		rect = pygame.Rect(i.x,i.y,50,50)
		if i.desiredMeal=='Waffles':
			pygame.draw.rect(screen, (255, 0, 0), rect)
		elif i.desiredMeal=='Potatoes':
			pygame.draw.rect(screen, (0, 255, 0), rect)
		elif i.desiredMeal=='Bread':
			pygame.draw.rect(screen, (0, 0, 255), rect)
	# print("")
	textsurface=myfont.render("Money: "+str(money),False,(255,255,255))
	screen.blit(textsurface,(5,5))
	for i in range(len(mealList)):
		textsurface=myfont.render(mealList[i]+str(stock[mealList[i]]),False,(255,255,255))
		screen.blit(textsurface,(5,(i+1)*15))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()
