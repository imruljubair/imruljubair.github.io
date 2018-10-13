
# Deleting keys from dictionary


card = {}
for letter in ['A', 'B', 'C']:
    # Start with an empty list for the letter
   card[letter] = []

for k in card:
   card[k] = [1,2,3,4]

print(card)

del card['B']

print(card)
