def main():
   first_name = input('Enter First Name: ')
   last_name = input('Enter Last Name: ')
   N = reverse_name(first_name, last_name)
   print('Reverse: '+str(N))
    
def reverse_name(first, last):
   name = last+' '+ first
   return name

main()
