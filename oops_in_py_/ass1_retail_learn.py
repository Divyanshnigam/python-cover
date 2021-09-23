import random
lo=[]
class customer:
    def setdetail(self):
        self.id=str(self)
        self.tele=int(input("Enter tele no. :"))

l=[]
c1=customer()
c1.setdetail()
c2=customer()
c2.setdetail()
c3=customer()
c3.setdetail()
c4=customer()
c4.setdetail()
list=[c1,c2,c3,c4]
for i in list:
    l.append(i.id[28:-1])
    l.append(i.tele)
print(l)

