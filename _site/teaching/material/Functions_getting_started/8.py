def main():
    # calls calgary() function
    calgary()

    # calls toronto() function
    toronto()

def calgary():
    birds1 = 700 # variable birds is used here, value assigned 700
    print('calgary has ', birds1, 'birds')

def toronto():
    birds2 = 590 # variable birds is also used here, but with value 590
    print('toronto has ', birds2, 'birds')

    # variable1 birds is local to calgary()
    # variable2 birds is local to toronto()


main()
