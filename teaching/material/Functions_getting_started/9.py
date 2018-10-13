# This program will show error....
def main():
    # calls calgary() function
    calgary()

    # calls toronto() function
    toronto()

def calgary():
    birds1 = 700 # 
    print('calgary has ', birds2, 'birds')
    # Error! Cause birds2 is not local to calgary()

def toronto():
    birds2 = 590 
    print('toronto has ', birds1, 'birds')
    # Error! Cause birds1 is not local to toronto()


main()
