class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, a, b):
        self.a=a
        self.b=b
        print(self.a + self.b)

    def subs(self,a,b):
        self.a=a
        self.b=b
        print(self.a - self.b)

class ch(calc):
    def mult(self,a,b):
        self.a=a
        self.b=b
        print(self.a * self.b)
    def divide(self,a,b):
        self.a=a
        self.b=b
        print(self.a // self.b)
c=ch(2,3) #get parent argument
print(c.add(2,3))
print(c.subs(2,3))
print(c.mult(2,3))
print(c.divide(2,3))


