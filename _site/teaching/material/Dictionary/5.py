
# Adding list as values for keys..... (continued)



card = {}
for letter in ["A", "B", "C"]:
   card[letter] = []

   card['A'] = [1,2,3,4]
   card['B'] = [5,6,7,8]
   card['C'] = [9,10,11,12]

x = card['B'][1]
print(x)
