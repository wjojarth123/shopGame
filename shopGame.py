import pygame
import time
import random
from enum import Enum
pygame.init()
screen = pygame.display.set_mode((800, 600))
mealList=['Bread','Potatoes']
possibleFoods = ['Bread', 'Potatoes', 'Waffles']
Done=False

CustomerState = Enum('CustomerState', 'onStreet goingToShop inShop goingUpShop leavingShop')

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
	for c in customers:
		if not c.state == 'CustomerState.onStreet':
			c.y += 1
		elif c.state == 'CustomerState.goingToShop':
			c.x += 1

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
	if time.time()-customerSpawnTime>=5:
		generateCustomer()
		customerSpawnTime=time.time()
	rect = pygame.Rect(550,150,200,300)
	pygame.draw.rect(screen, (0, 150, 50), rect)
	moveCustomers()
	for i in customers:
		if i.y==360 and i.desiredMeal in mealList and i.state == 'CustomerState.onStreet':
			print("yay! a customer entered with the meal of: " + i.desiredMeal)
			i.state = CustomerState.goingToShop
		if i.x==600:
			x
		# print(i)

		rect = pygame.Rect(i.x,i.y,50,50)
		pygame.draw.rect(screen, (250, 100, 50), rect)
	# print("")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()
