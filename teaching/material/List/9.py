# multidimensional list
# Example 9.1

students = [['Joe', 'Kim'], ['Sam', 'Sue'], ['Kelly', 'Chris']]
print(students[1])


# Example 9.2
for n in students:
    print(n)

# Example 9.3
a,b = students.pop()
print(a,' ',b)

# Example 9.4
students.append(['x','y'])
print(students)
