import socket

tilemap = []
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
	tilemap[20][4]=7
makeTileMap()
