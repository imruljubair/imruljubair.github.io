from SimpleGraphics import *

counter = 0;
setColor('black')
while counter <=4:
    xValue = int(input('Enter X coordinte: '))
    yValue = int(input('Enter Y coordinte: '))

    ellipse(xValue, yValue, 10,10)
    counter = counter + 1

