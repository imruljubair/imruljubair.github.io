
# Some methods that might be useful....

entry = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

#........... get()..............
# returns value

val = entry.get('Andy','Not found\n')
print(val)
val = entry.get('Katie','Not found\n')
print(val)

print("")

#........... items()..............
# returns key with associated values

for key, value in entry.items():
   print(key, value)

print("")

#........... keys() ...............
# Returns all keys
for k in entry.keys():
   print(k)

print("")


#........... values() ...............
# Returns all values
for k in entry.values():
   print(k)

print("")

#........... clear() ........
entry.clear()
print(entry)
