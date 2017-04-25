#Exercise 1, read a file
def readFile():
    fileName = input('Please enter the filename of the file you want to read; please remember to include extensions: ')
    file_handle = open(fileName, 'r')
    print(file_handle.read())
#Exercise 2, create a file and write to it
def createFile():
    fileName = input('Please enter the filename of the file you want to create: ')
    file_handle = open(fileName, 'w')
    userWrite = input('PLease enter the text you would like to add to the file: ')
    file_handle.write(userWrite)
#Exercise 3, histogram of file contents for letter and word
def histogram():
    file_handle = open(input('Please enter the filename of the file you want to analyze: '), 'r')
    fileContents = file_handle.read() #Stores file contents in variable
    letterBreakdown = list(fileContents) #Splits contents in to list by character
    letterCount = {}
    wordCount = {}
    for x in range(len(letterBreakdown)): #Populates empty dictionay with counts of letters
        letterCount[letterBreakdown[x]] = letterBreakdown.count(letterBreakdown[x])
    print('Breakdown of character occurences:\n',letterCount)
    wordBreakdown = fileContents.split(' ') #Splits contents in to list by word (Space delimited)
    for x in range(len(wordBreakdown)):
        wordCount[wordBreakdown[x]] = wordBreakdown.count(wordBreakdown[x])
    print('Breakdown of word occurences:\n', wordCount)

#Exercise 4, 
def jsonWrite():
    data = {
        'data':[[1, 2], [3, 4], [5, 6], [7, 8]]
        }
    with open('test.json', 'w') as fh:
        json.dump(data, fh)

def jsonOpen():
    with open('test.json', 'r') as f:
        data = json.load(f)
        print(data)
