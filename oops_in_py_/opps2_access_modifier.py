# Restrictions to inheritance to inherit one and other to not
class c1:
    def __init__(self,a,b,c):
        self.a=a #public
        self._b=b #protected
        self.__c=c #private
class ch(c1):
    pass

c=ch(1,2,3) #get parent argument
print(c.a)
print(c._b)

print(c._c1__c) #name of obj_name. name of parent class__private class... thru this private is accessed by special syntax.
print(c.__c) #private