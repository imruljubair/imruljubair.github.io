# pop(), insert() and remove()
# Example 8.1

my_list = [10, 20, 30, 30, 40]
print('List :' + str(my_list))

x = my_list.pop()
print('You have popped: '+str(x))

print('List items after popping: '+str(my_list))

# Example 8.2

my_list.insert(1,100)
print('List after inseting: '+str(my_list))

# Example 8.3

my_list.remove(30)
print('List after removing: '+str(my_list))
