# The 'in' operator and 'index'
# Example 6.1

def main():
    prod_nums = ['v47', 'f89y', 'y6t', 'w788']

    search = input('Enter a product to search: ')

    if search in prod_nums:
        print(search + ' found at ' + str(prod_nums.index(search)))
    else:
        print(search + ' not found')

main()
