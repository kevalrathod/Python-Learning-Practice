#instant Methods

class Dog:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Description(self, breed):
        return "Dog name is {} and breed is {}".format(self.name,breed)
        
    def Speak(self , sound):
        return 'Dog name is {} and sound is{}'.format(self.name,sound)
        

mike = Dog("Mike", 10)
print(mike.Description("labradore"))
print(mike.Speak("bho bhow"))