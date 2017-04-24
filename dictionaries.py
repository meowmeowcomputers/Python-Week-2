#Exercise 1
def dictEx1():
    phonebook_dict = {
        'Alice': '703-493-1834',
        'Bob': '857-384-1234',
        'Elizabeth': '484-584-2923'
    }
    print(phonebook_dict['Alice'])
    phonebook_dict['Kareem'] = '938-489-1234'
    del phonebook_dict['Alice']
    phonebook_dict['Bob'] = '968-345-2345'
    print(phonebook_dict)

#Exercise 2
def dictEx2():
    ramit = {
      'name': 'Ramit',
      'email': 'ramit@gmail.com',
      'interests': ['movies', 'tennis'],
      'friends': [
        {
          'name': 'Jasmine',
          'email': 'jasmine@yahoo.com',
          'interests': ['photography', 'tennis']
        },
        {
          'name': 'Jan',
          'email': 'jan@hotmail.com',
          'interests': ['movies', 'tv']
        }
      ]
    }
    print(ramit['email'])
    print(ramit['interests'][0])
    print(ramit['friends'][0]['email'])
    print(ramit['friends'][1]['interests'][1])

#Letter Summary Exercise
word = input('Enter string to count each letter: ')
def letter(word):
    lettercount = {'a': word.count('a'), 'b': word.count('b')}
    print(lettercount)
letter(word)

#Word Count Summary Exercise

def wordCount(para):
    paraWordCount = {} #Defines empty dictionary
    newPara = para.split(' ') #Splits inputted paragraph in to list
    for x in range(len(newPara)): #For loop to assign word counts to dictionary
        paraWordCount[newPara[x]] = newPara.count(newPara[x])
    print(paraWordCount)

if __name__ = '__main__':
    dictEx1()
    dictEx2()
