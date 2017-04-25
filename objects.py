#Exercise 1

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friendsList = []
        self.greetCount = 0
    def greet(self, other_person):
        print('Hello {0}, I am {1}!'.format(other_person.name, self.name))
        self.greetCount += 1
    def printProfile(self):
        print('Name:{} Email:{} Phone Number:{} '.format(self.name, self.email, self.phone))
    def addFriends(self, buddy):
        self.friendsList.append(buddy)
    def numFriends(self):
        print(len(self.friendsList))
    def countGreets(self):
        print('There were {} greets'.format(self.greetCount))
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)


sonny = Person('Sonny', 'sonny.das@hotmail.com', '281-223-5566')
jordan = Person('Jordan', 'jordan.speith@utexas.edu', '512-200-2000')
sonny.greet(jordan) #Sonny greeting Jordan
#jordan.greet(sonny) #Jordan greeting Sonny

print(sonny.email) #Print Sonny's email

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def printInfo (self): #Method to print out car info
        print('{} {} {}'.format(self.year, self.make, self.model))

ryanCar = Vehicle('Toyota', '4Runner', '2006')
leslieCar = Vehicle('Volkswagen', 'Golf', '2012')
leslieCar.printInfo() #Prints out info
