#inheritance Example


#parent class
class Dog:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
# Child class 
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
# Child class 
class Bulldog(Dog):
    def run(self, speed):\
        return "{} runs {}".format(self.name, speed)

#Object initialization
jim = Bulldog("Jim", 12)
lax = RussellTerrier("lax",14)

print(jim.description())
print(jim.speak("bhooobhoo"))
print(jim.run("slowly"))

print(lax.description())
print(lax.speak("bhow bhow"))
print(lax.run("fast"))