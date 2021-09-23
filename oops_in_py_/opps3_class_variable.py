class emp:
    count=0
    def __init__(self):
        emp.count = emp.count+1  # class variable written with class variable name
    def disp(self):
        print(emp.count)
e1=emp() # incremented count
e2=emp() # incremented count
e2.disp() # any object can display incremented greatest value..

