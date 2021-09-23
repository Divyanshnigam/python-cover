class student:
    def details(self,name,internal,external):
        self.name=name
        self.internal=internal
        self.external=external
        print(self.name,end=' ')
        if (self.internal+self.external) >= 60:
            print("pass and obtained:", self.internal+self.external)
        else:
            print("Fails and obtained: ", self.internal+self.external)
details1=student() #declaration with the class
details1.details("rohit",30,40)
details2=student()
details2.details("danish",30,20)

