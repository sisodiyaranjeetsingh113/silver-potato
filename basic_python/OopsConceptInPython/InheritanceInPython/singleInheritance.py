class A:
    def __init__(self,name):
        self.name=name
    def getName(self):
        print("Name :",self.name)
class B(A):
    def __init__(self,name,password):
        super().__init__(name)
        self.password=password
    def getPassword(self):
        print("Password :",self.password)
Baby=B("Ranjeet","Ranjeet123")
Baby.getName()
Baby.getPassword()