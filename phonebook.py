def lookupEntry():
    fileHandler = open('entries.txt', 'r')
    contents = fileHandler.read() #Loads contents of file in to variable
    blockList = contents.split(',') #Splits entires in to '"Name": "Number"' list

    for x in range(len(blockList)): # Splits name and number
        blockList[x] = blockList[x].upper().split(':')

    phoneDict = {} #Populates dictionary with entries
    for x in range(len(blockList)):
        for y in range(len(blockList[x])):
            if y % 2 == 0:
                phoneDict[blockList[x][y]] = blockList[x][y+1]

    lookup = input('Enter the (first) name of the person whose number you\'re looking for: ').upper()

    if lookup in list(phoneDict.keys()): #Looks up user input in dictionary
        print('\nName: ', lookup)
        print('Phone Number: ', phoneDict[lookup],'\n')
        again()
    else:
        print('Name not found!')
        again()

def again():
    again = input('Continue using Phonebook? (y/n)').upper()
    if again == 'Y':
        phonebook()
    elif again == 'N':
        print('Bye!')
        exit()
    else:
        print('Please enter a valid response(y/n)')
        again()

def setEntry():
    fileHandler = open('entries.txt', 'a')
    name = input('Please enter a name to add to Phonebook: ')
    number = input('Please enter a phone number: ')
    fileHandler.write(',{0}:{1}'.format(name,number))
    fileHandler.close()
    again()

def deleteEntry():
print('Delete')
    fileHandler = open('entries.txt', 'r')
    contents = fileHandler.read() #Loads contents of file in to variable
    blockList = contents.split(',') #Splits entires in to '"Name": "Number"' list

    for x in range(len(blockList)): # Splits name and number
        blockList[x] = blockList[x].upper().split(':')

    phoneDict = {} #Populates dictionary with entries
    for x in range(len(blockList)):
        for y in range(len(blockList[x])):
            if y % 2 == 0:
                phoneDict[blockList[x][y]] = blockList[x][y+1]
    

def listEntry():
    print('list)')

def phonebook():
    options = {
        '1': lookupEntry,
        '2': setEntry,
        '3': deleteEntry,
        '4': listEntry,
        '5': exit
        }

    try:
        print('Electronic Phone Book')
        print('=====================')
        choice = input('1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit\n')
        options[choice]()
        phonebook()
    except ValueError:
        print('\n**********************\n*Enter a valid number*\n**********************\n\n\n\n')
        phonebook()
    except KeyError:
        print('\n**********************\n*Enter a valid number*\n**********************\n\n\n\n')
        phonebook()

phonebook()
