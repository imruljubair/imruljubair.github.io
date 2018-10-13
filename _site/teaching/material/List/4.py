# Using length
# Example 4.1

my_list = [10, 20, 30, 40]
size = len(my_list)
print(size)

# Example 4.2

index = 0
while index < len(my_list):
    print(my_list[index])
    index = index + 1

# Example 4.3

index = 0
while index < len(my_list):
    my_list[index] = my_list[index]+1
    index = index + 1
print(my_list);
