class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def _add(self, a, b):
        self.a=a
        self.b=b
        print(self.a + self.b)

    def __subs(self,a,b):
        self.a=a
        self.b=b
        print(self.a - self.b)

class ch(calc):  #chaild class
    def mult(self,a,b):
        self.a=a
        self.b=b
        print(self.a * self.b)
    def divide(self,a,b):
        self.a=a
        self.b=b
        print(self.a // self.b)
c=ch(2,3) #get parent argument
print(c._add(2,3))
# print(c.__subs(2,3))  # private class funct and can't be accessed
print(c._calc__subs(2,3))  # private class funct but access with special syntax

print(c.mult(2,3))
print(c.divide(2,3))


