
# string matching with dictionay


card = {}
for letter in ['A', 'B', 'C', 'D', 'E']:
    # Start with an empty list for the letter
   card[letter] = []


card['A'] = [1,2]
card['B'] = [3,4]
card['C'] = [5,6]
card['D'] = [7,8]
card['E'] = [9,10]

word = 'BED'

for x in range(len(word)):
   letter = word[x]
   if letter in card:
      print(letter, card[letter])

