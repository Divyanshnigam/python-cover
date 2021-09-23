class computer:
    def writecode(self,text):
        print(text,"written in editor")
    def execute(self):
        print("code executed")
class student:
    def dolabassignment(self,computer,assignment):
        computer.writecode(assignment)
        computer.execute()
c=computer()
s=student()
s.dolabassignment(c,"Assignment code")
# Association ex- student solves lab assignment using computer
