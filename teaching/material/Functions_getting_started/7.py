def main():
    # calls calgary() function
    calgary()

    # calls toronto() function
    toronto()

def calgary():
    birds = 700 # variable birds is used here, value assigned 700
    print('calgary has ', birds, 'birds')

def toronto():
    birds = 590 # variable birds is also used here, but with value 590
    print('toronto has ', birds, 'birds')

    # birds variable is distinct for two different function!
    # variable birds in calgary() is not the variable birds in toronto()
    # these are local variable

    # variable birds is local to calgary()
    # another variable birds is local to toronto()


main()
