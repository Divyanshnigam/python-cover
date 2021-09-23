class A:
    def f1(self):
        print("A")

class B:
    def f2(self):
        print("B")

class C:
    def f3(self):
        print("C")

class ch(A,B,C): # this order A B C does changes
    pass
och =ch()
och.f1() # order matters
och.f3()