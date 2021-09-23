class Student:
    def __init__(self, name): #__init__ initialised at the time of creation
        self.name = name

    def getname(self):
        return self.name

#   def __init__(self,name):
#       self.name=name
#       print(self.name) .....
#s1=Student("amit")..  initialise and print, without getter function.. The paraenthesis calls for __init__



s1=Student("amit") # assigned automatically..
print(s1.getname())