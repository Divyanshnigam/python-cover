# to overload an * operator
class A:
    def __init__(self,a):
        self.a=a
    # multiplying two objects
    def __mul__(self, o):
        return (self.a * o.a)
ob1=A(8)
ob2=A(2)
print(ob1 * ob2) # * automatically calls for __mul__
