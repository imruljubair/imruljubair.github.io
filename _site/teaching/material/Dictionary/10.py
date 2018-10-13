
# string matching with dictionay


card = {'A' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4,
        'E' : 5,
        'F' : 6}


x = input("Enter any word with the letter A~E: ")
word = x.upper() 

for x in range(len(word)):
   letter = word[x]
   print(letter, card[letter])

