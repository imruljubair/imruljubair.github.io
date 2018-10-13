
# Adding list as values for keys.....
# Using 'in' and 'not in' to find keys in dictionary


card = {}
for letter in ['A', 'B', 'C']:
    # Start with an empty list for the letter
   card[letter] = []

for k in card:
   card[k] = [1,2,3,4]

print(card)

if 'B' in card:
   print('Found')

if 'Z' not in card:
   print('not found')
