import random
import pygame
pygame.font.init()
myfont=pygame.font.SysFont('Times New Roman',24)
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

	def handleKeypress(self, event):
		global text
		global priceOfitem
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				print(text)
				print(text.title() in self.prices)
				print(self.prices)
				if text.title() in self.prices:
					priceOfitem=self.prices[text.title()]
					self.item=text.title()
					print('Just set trader item to: ' + self.item)
					print(text)

				text=''

			elif event.key == pygame.K_BACKSPACE:
				text = text[:-1]
			else:
				text += event.unicode

text=''

def generateTrader(x, y, possibleFoods, rect):
	traderPrices = {}
	for food in possibleFoods:
		traderPrices[food] = random.randrange(10,50)
	traderPrices['Ad'] = 50
	trader = Trader(traderPrices,x,y,rect)
	return trader
def trade(trader, screen):
	windowrect=pygame.Rect(550,10,200,100)
	pygame.draw.rect(screen,(255,255,255),windowrect)
	buyrect=pygame.Rect(650,60,80,30)
	pygame.draw.rect(screen,(0,255,100),buyrect)
	textsurface=myfont.render("product: "+text,False,(180,0,180))
	screen.blit(textsurface,(560,20))
	textsurface=myfont.render("price: "+str(priceOfitem),False,(180,0,180))
	screen.blit(textsurface,(560,60))


priceOfitem=0
