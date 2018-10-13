# assiging value in a functionto a global variable in a function
number = 0

def main():
   global number
   number = int(input('Enter a number: '))
   show_number()

def show_number():
   print('Global variable is changed to : ', number)


main()
