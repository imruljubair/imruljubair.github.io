from SimpleGraphics import *

def main():
    
    img = loadImage("2.ppm")
    new_image = createImage(getWidth(img), getHeight(img))
    
    for y in range(0, getHeight(img)):
        for x in range(0,getWidth(img)):

            r, g, b = getPixel(img, x, y)
            pixel = rgb2gray(r, g, b) #calling rgb2gray() functon with 3 paramterers
            putPixel(new_image, x,y, pixel, pixel, pixel);
                
    drawImage(new_image, 0, 0)

# definition of rgb2gray function()
def rgb2gray(red, green, blue):
    gray = (red+green+blue)/3
    return gray #returning it

main()

