'''
class c1:
    @staticmethod
    def fun(a,b):  # no need of any argument
        print("hello")
c1.fun(5,5)
'''

# Instancemethod holds the current address of all arguments
# staticmethod import without any object and no need of any argument
# Classmethod import without any object but 1 argument is compulsary
class c1:
    @classmethod
    def fun(cls):   # atleast 1 argument must be there to track the classs  ..  cls is not a keyword
        print("hello")
c1.fun()
