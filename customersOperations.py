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
