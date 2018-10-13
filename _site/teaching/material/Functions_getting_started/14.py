def main():
   x = anyFunction(12)
   print("the number is", x) 

def anyFunction(aNumber):
    if aNumber%2==0:
        return 'even'
    elif aNumber%2 != 0:
        return 'odd'

main()
