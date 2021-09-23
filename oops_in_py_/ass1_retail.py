import random
lo=[]
class customer:
    def setdetail(self):
        self.name=input("Enter name")
        self.tele=int(input("Enter tele no. :"))
    def getdetail(self):
        l = []
        l.append(self.name)
        l.append(self.tele)
        l.append(random.randint(1, 10))
        lo.append(l)
        print(l)


c1 = customer()
c1.setdetail()
c1.getdetail()

c2 = customer()
c2.setdetail()
c2.getdetail()

c3 = customer()
c3.setdetail()
c3.getdetail()

c4 = customer()
c4.setdetail()
c4.getdetail()

print(lo)