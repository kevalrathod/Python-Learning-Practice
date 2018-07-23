#overidding Polymorphism

class ABC:
	def Speak(self):
		print("afakfh")
class XYZ:
	def Speak(self):
		print("gaduia")
def typesOfSpeak(spktyp):
	spktyp.Speak()

obj1 = ABC()
obj2 = XYZ()

typesOfSpeak(obj1)
typesOfSpeak(obj2)