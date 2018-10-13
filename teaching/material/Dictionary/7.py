
# Adding keys and values in dictionary
# Modifying keys and values in dictionary


card = {}
for letter in ['A', 'B', 'C']:
    
   card[letter] = []

for k in card:
   card[k] = [1,2,3,4]

print(card)

card['D'] = [5,6,7]
card['A'] = [8,9,10]

print(card)
