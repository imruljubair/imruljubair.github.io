# this code finds the keys in a dictionary that are not in the values

def theDictionary():
    dictionary = {'a':['b','d','e'],
                  'b':['f','g'],
                  'c':['e']}

    return dictionary

  

def theFunction(dictionary):

    listOfAllValue = []
    for key in dictionary:
        for value in dictionary[key]:
            if value not in listOfAllValue:
                listOfAllValue.append(value) 
    
    for key in dictionary:
        if key not in listOfAllValue:
            print('\t',key)


def main():
    dictionary = theDictionary()

    print('the dictionary :')
    for key in dictionary:
        print(key,' : ', dictionary[key])

    print('keys in a dictionary that are not in the values :')
    theFunction(dictionary)

main()
