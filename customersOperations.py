import random
from enum import Enum
CustomerState = Enum('CustomerState', 'onStreet goingToShop waiting leavingShop')
class Customer:
	x=-10
	y=210
	budget = 5
	desiredMeal = ['Waffles']
	state = CustomerState.onStreet
	def __init__(self, desiredMeal, budget):
		self.budget=budget
		self.desiredMeal=desiredMeal
		#self.x += random.randrange(-20, 40)

	def __str__(self):
		return str(self.x)+", "+str(self.y)+", "+str(self.budget)+", "+self.desiredMeal


def generateCustomer(possibleFoods):
	customer = Customer(possibleFoods[random.randrange(0,len(possibleFoods))],random.randrange(2,50))
	#print(customer)

	return customer
