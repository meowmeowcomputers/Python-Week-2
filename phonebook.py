def lookupEntry():
    print('lookup')
def setEntry():
    print('setEntry')
def deleteEntry():
    print('Delete')
def listEntry():
    print('list)')

LISTING = {}

def phonebook():
    options = {
        '1': lookupEntry,
        '2': setEntry,
        '3': deleteEntry,
        '4': listEntry,
        '5': quit
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
