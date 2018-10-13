#Using variables from function to function

def main():
    get_name()
    print('Hi, ', name) # this will cause an error
    print('welcome')

def get_name():
    name = input('enter your name: ')

main()
