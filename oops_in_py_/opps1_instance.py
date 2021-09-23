class calc:
    def sum1(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)
    def sub1(self ,a ,b):
        self.a=a
        self.b=b
        print(self.a-self.b)
calc1=calc()
calc1.sum1(4, 4)
calc2=calc()
calc2.sum1(5, 6)
calc3=calc()
calc2.sub1(5, 6)

# In instance first method is refers to the current obj address
