import random
import pygame
breadImage=pygame.image.load("bread.png")
potatoImage=pygame.image.load("potato.png")
wafflesImage=pygame.image.load("waffles.png")
chickenImage=pygame.image.load("chicken.png")
soupImage=pygame.image.load("soup.png")
roastImage=pygame.image.load("roastbeef.png")
sushiImage=pygame.image.load("sushi.png")
iceCreamImage=pygame.image.load("iceCream.png")
spaghettiImage=pygame.image.load("Spaghetti.png")
pizzaImage=pygame.image.load("pizza.png")
adImage=pygame.image.load("ad.png")

buyImage=pygame.image.load("buy.png")
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
			traderPrices[food] = random.randrange(5,30)
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
	makeitem(pizzaImage,10 + offset*3,trader,"Pizza",screen)
	makeitem(spaghettiImage,10 + offset*4,trader,"Spaghetti",screen)
	makeitem(sushiImage,10 + offset*5,trader,"Sushi",screen)
	makeitem(roastImage,10 + offset*6,trader,"Roast Beef",screen)
	makeitem(iceCreamImage,10 + offset*7,trader,"Ice Cream",screen)
	makeitem(chickenImage,10 + offset*8,trader,"Chicken",screen)
	makeitem(soupImage,10 + offset*9,trader,"Soup",screen)
	makeitem(adImage,10 + offset*10,trader,"Ad",screen)

priceOfitem=0
