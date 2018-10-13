# There can be many functions in a program
# A function ca be called within another function
# Example

# define daddy() function
def daddy():
    print('Daddy says: boy, where are you?')
    boy()
    print('Daddy says: go to sleep')

# Define boy() function
def boy():
    print('boy says: daddy, I am here...')

# Now call main()
# main will call message()

daddy()
