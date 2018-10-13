position = int(input("Please enter the position you want to know: "))
a = 0
b = 1

for i in range(2,position+1):
  number = a + b
  a = b
  b = number
print("The ",position,"th fibonacci number is ",number)  

