number=int(input("Please enter a number: "))

binaryStr = ''
    
while number>0:
    result=int(number/2)
    remainder=number%2
    binaryStr =str(remainder)+binaryStr
    number=result

print("Answer is : " + binaryStr)
