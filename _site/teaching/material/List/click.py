from SimpleGraphics import * 

img = loadImage("unsparkling-vampire.gif")
resize(getWidth(img), getHeight(img))
drawImage(img, 0, 0)

pixel_list = []

draw = False
while (draw==False):
    update()
    if (leftButtonPressed()==True):
        x,y = mousePos()
        r,g,b = getPixel(img, x,y)
        if r==0 and g == 255 and b == 0:
            pixel_list.append([x,y])
            print(pixel_list)
            putPixel(img, x,y, 0,0,0)
        update()
