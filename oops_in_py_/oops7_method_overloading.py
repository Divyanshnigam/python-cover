# METHOD OVERLOADING

class c1:
    def f1(self,*a):
        if len(a)==0:
            print("Zero")
        elif len(a)==1:
            print("one")
        elif len(a)==2:
            print("two")
        elif len(a)==3:
            print("Three")
        else:
            print("else")
o=c1()
o.f1()
o.f1(30)
o.f1(4,5)
o.f1(5,6,7)
o.f1(8,9,10,11)