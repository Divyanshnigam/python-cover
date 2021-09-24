# POLYMORPHISM
# Means having more than one form
'''
examples of polymorphism in oops
1. METHOD OVERRIADING
2. METHOD OVERLOADING
3. OPERATOR OVERLOADING
'''
# METHOD OVERRIDING -- Parent child relationship
class c1:
    def f1(self):
        print("f1 of parent")
class ch(c1): # same method name f1 with different
    def f1(self):
        print("f1 of child")

o=c1()
o.f1() # f1 of parent

och=ch()
och.f1() # f1 of child
