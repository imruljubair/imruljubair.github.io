from SimpleGraphics import *

counter = 1;
setColor('black')



while counter <=5:
    xValue = int(input('Enter X coordinte: '))
    yValue = int(input('Enter Y coordinte: '))

    ellipse(xValue, yValue, 10,10)
    
    if counter <=1:
        prevX = xValue
        prevY = yValue
    else:
        line(prevX, prevY, xValue, yValue)
        prevX = xValue
        prevY = yValue
        
    counter = counter + 1
