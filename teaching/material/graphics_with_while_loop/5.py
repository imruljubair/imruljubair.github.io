from SimpleGraphics import *

counter = 1;
setColor('black')

prevX = 0;
prevY = 0;

while counter <=3:
    xValue = int(input('Enter X coordinte: '))
    yValue = int(input('Enter Y coordinte: '))

    ellipse(xValue, yValue, 10,10)
  

    line(prevX, prevY, xValue, yValue)
    prevX = xValue
    prevY = yValue

    counter = counter + 1

