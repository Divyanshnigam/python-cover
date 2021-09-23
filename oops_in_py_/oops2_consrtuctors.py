class A(object): # child class of object
    def __new__(cls):
        print("new called")
        return super(A,cls).__new__(cls)
    def __init__(self):
        print("__init__ called")
o=A()
