class Student:
    def f1(self, name): #__init__ initialised at the time of creation
        self.name = name
class st(Student):  #st is child class of Student..inheritance
    def f2(self,age):
        self.age=age
s1=st()
s1.f1("amit")
s1.f2(30)
