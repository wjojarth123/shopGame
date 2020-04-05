from PIL import Image
#imglist[green,shopright,shopleft,shopdown,shopup,houseright,houseleft,housedown,houseup,leftT,rightT,FW,upright,downright,downleft,upleft,vertroad,horiroad]
im = Image.open('New Piskel-1.png.png') # Can be many different formats.
pix = im.load()
green=(71, 255, 0, 255)
red=(255, 56, 0, 255)
black=(0,0,0,255)
purple=(161, 0, 255, 255)
map=[]
for x in range(im.size[0]):
    row=[]
    for y in range(im.size[1]):
        # grass
        if pix[x,y]==green:
            row.append(0)
        #house+shop
        elif pix[x,y]==red:
            if pix[x+1,y]==black:
                row.append(1)
            elif pix[x-1,y]==black:
                row.append(2)
            elif pix[x,y+1]==black:
                row.append(3)
            elif pix[x,y-1]==black:
                row.append(4)
        elif pix[x,y]==purple:
            if pix[x+1,y]==black:
                row.append(5)
            elif pix[x-1,y]==black:
                row.append(6)
            elif pix[x,y+1]==black:
                row.append(7)
            elif pix[x,y-1]==black:
                row.append(8)
        #road
        elif pix[x,y]==black:
            if pix[x,y+1]==black and pix[x,y-1]==black and pix[x-1,y]==black and not pix[x+1,y]==black:
                row.append(9)
                #left T
            elif pix[x,y+1]==black and pix[x+1,y]==black and pix[x-1,y]==black and not pix[x,y-1]==black:
                #down t
                row.append(18)
            elif pix[x,y-1]==black and pix[x,y-1]==black and pix[x+1,y]==black and not pix[x,y+1]==black:
                #up T
                row.append(19)
            elif pix[x,y+1]==black and pix[x,y-1]==black and pix[x+1,y]==black and not pix[x-1,y]==black:

                #right T
                row.append(10)
            elif pix[x-1,y]==black and pix[x+1,y]==black and pix[x,y+1]==black and pix[x,y-1]==black:
                #  |
                #__ __
                #  |
                row.append(11)
            elif pix[x,y+1]==black and pix[x+1,y]==black:
                # _
                #|
                row.append(12)
            elif pix[x,y-1]==black and pix[x+1,y]==black:
                #|_
                row.append(13)
            elif pix[x,y-1]==black and pix[x-1,y]==black:
                #_|
                row.append(14)
            elif pix[x,y+1]==black and pix[x-1,y]==black:
                #_
                # |
                row.append(15)
            elif pix[x,y+1]==black or pix[x,y-1]==black:
                #|
                print("putting road")
                row.append(16)
            elif pix[x+1,y]==black or pix[x-1,y]==black:
                #_
                print("putting road")
                row.append(17)
            else:
                print("roadfail")
        else:
            print("fail all")
            print(pix[x,y])
    print(len(row))
    map.append(row)
print()
print(len(map))

print(map)
