# abstract class -> if method has no block (p-c p should be abst class abc ) # is a decorator
from abc import ABC,abstractmethod
class myabsclass(ABC):  # abstract class containg
    @abstractmethod                            # abstraction method
    def fun(self):
        # print("abstract method") .. not to write
        pass
    def fun2(self):
        print("simple method or non abstract method")
class ch(myabsclass): # child class .. # not a abstract class becoz not having abstract method
    def fun(self):      #every abstact class must be implemented in the child class
        print("full method")
    def myfun(self):
        print("myfun")
och=ch() # called only child class. abstraction putting restrictions
och.fun()