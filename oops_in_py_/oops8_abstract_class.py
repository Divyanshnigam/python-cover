# abstract class ->An abstract class can be considered as a blueprint for other classes.
# It allows you to create a set of methods that must be created within any child classes built from the abstract class.
# A class which contains one or more abstract methods is called an abstract class.
# An abstract method is a method that has a declaration but does not have an implementation. # is a decorator
from abc import ABC,abstractmethod
class myabsclass(ABC):  # abstract class must containg
    @abstractmethod                            # atleast one abstraction method
    def fun(self):
        # print("abstract method") .. not to write
        pass
    def fun2(self):
        print("simple method or non abstract method")
class ch(myabsclass): # child class .. # not a abstract class becoz not having abstract method
    def fun(self):      #every abstract class must be implemented in the child class
        print("full method")
    def myfun(self):
        print("myfun")
och=ch() # called only child class. abstraction putting restrictions
och.fun()