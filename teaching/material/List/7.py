# append()
# Example 7.1

def main():
    name_list = []
    again = 'y'

    while again == 'y':

        name = input("Enter a name : ")
        name_list.append(name)

        print('Do you want to add another name ?')
        again = input('y = yes, anything else = no: ')
        print()

    print('The names you have listed: ')

    for name in name_list:
        print(name)

main()
