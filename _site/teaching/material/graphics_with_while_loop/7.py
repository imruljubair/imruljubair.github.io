from SimpleGraphics import *

counter = 1;
setColor('black')
line(0,300,800,300)

xPos = 200
while counter <=4:
  
    height = int(input('Enter the height of your column/bar: '))
    

    rect(xPos,300,5, height)

    xPos = xPos + 20
    counter = counter + 1
