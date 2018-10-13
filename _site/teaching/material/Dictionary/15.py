# this code finds the values in a dictionary that are not in the keys

def theDictionary():
    dictionary = {'a':['b','d','e'],
                  'b':['f','g'],
                  'c':['e']}

    return dictionary

  

def theFunction(dictionary):
    
    listOfAllValues = []
    for key in dictionary:
        for value in dictionary[key]:
            if value not in listOfAllValues:
                listOfAllValues.append(value) 


    
    uniqueList = []
    for x in listOfAllValues:
        if x not in dictionary:
            uniqueList.append(x)
            print('\t', x)


def main():
    dictionary = theDictionary()
    print('the dictionary :')
    for key in dictionary:
        print(key,' : ', dictionary[key])

    print('values in a dictionary that are not in the keys :')
    theFunction(dictionary)

main()
