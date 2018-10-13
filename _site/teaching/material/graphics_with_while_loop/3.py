from SimpleGraphics import *


line(200,100,200,500)

counter = 1
xValue = 220
yValue = 50
data = 20

while counter <=5:
    text(xValue, yValue, data)
    yValue = yValue + 100
    data = data - 10


