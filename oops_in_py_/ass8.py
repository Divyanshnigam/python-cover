from abc import ABC,abstractmethod
class employee():
    salary=40000
    def gethours(self):
        pass
    def getsalary(self):
        pass
    def getvacationday(self):
        pass
    def getvactionform(self):
        pass
class Marketer():
    @abstractmethod
    def advertise(self):
        pass
class chm(Marketer):
    def advertise(self):
        print("Act now")
och=chm()
och.advertise()