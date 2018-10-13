# this code finds the values in a dictionary that is most frequently used

def theDictionary():
    dictionary = {'a':['g','b','d','e'],
                  'b':['f','g','g'],
                  'c':['e','g','b']}

    return dictionary

  

def theFunction(dictionary):
   
    listOfAllValues = []
    for key in dictionary:
        for value in dictionary[key]:
                listOfAllValues.append(value) 

    newList = []
 
    for x in listOfAllValues:
        count = 0
        for y in listOfAllValues:
            if x == y:
                count = count + 1
                newList.append((count,x))

    maxLen,value = max(newList)
    print(value, maxLen)
                



def main():
    dictionary = theDictionary()
    print('the dictionary :')
    for key in dictionary:
        print(key,' : ', dictionary[key])

    print('values in a dictionary that is most frequently used :')
    theFunction(dictionary)

main()
