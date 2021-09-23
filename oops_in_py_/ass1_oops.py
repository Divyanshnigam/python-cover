class customer:
    def setname(self):
        self.name=input("Enter name")     # ="amit"
    def getname(self):
        return self.name

c1=customer()
c1.setname()
print(c1.getname())  # print(c1.name)