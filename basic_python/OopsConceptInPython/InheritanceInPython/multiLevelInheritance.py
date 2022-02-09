class A1:
    def __init__(self,password):
        self.password=password
    def getPassword(self):
       print("Password :",self.password)
class A(A1):
    def __init__(self,name,password):
        super().__init__(password)
        self.name=name
    def getName(self):
        print("Name :",self.name)
class B(A):
    def __init__(self,name,number,password):
        super().__init__(name,password)
        self.number=number
    def getNumber(self):
        print("Number :",self.number)
b=B("aryan","7909815051","aryan123") 
b.getName()
b.getNumber()
b.getPassword()
