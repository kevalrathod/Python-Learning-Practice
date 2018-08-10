class Exception:
    def __init__(self, name):
        self.name=name
    def Add(self,a,b):
        try:
            self.a=a
            self.b=b
            return a/b
        except ZeroDivisionError:
            print("Divide by zero Error")
o1=Exception('First Add Something')
o2=o1.Add(4,0)
print(o2)
