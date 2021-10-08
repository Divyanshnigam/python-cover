class smallval(Exception):
    def __init__(self,arg):
        self.args = arg

class largeval(Exception):
    def __init__(self,arg):
        self.args = arg
try:
    a=int(input("Enter a Number"))
    if a<10:
        raise smallval("Value is small")
    if a>10:
        raise largeval("Value is large") # raise is used to raise the exception..
    else:
        print("yes the correct value is 10")
except smallval as e:
    print(type(e.args))
    for i in e.args:
        print(i,end="")
    print(e.args)
    print("\n")
except largeval as e:
    print(type(e.args))
    for i in e.args:
        print(i,end="")
    print(e.args) # printing in tuple format..
    print("\n")