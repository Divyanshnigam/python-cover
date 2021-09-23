#Super class

class student:

    # protected data members
    _name = None
    _roll = None
    _branch = None

    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch

    # protected member function
    def _displayRollRollAndBranch(self):
        #accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)

# derived class
class RAJAT(student):

    #constructor
    def __init__(self,name,roll,branch):
        student.__init__(self,name,roll,branch)

    # public member function
    def displayDetails(self):
        #accessing proctected data members of super class
        print("Name: ",self._name)

        #accessing protected data members

