class MathematicalOperation:
    add=0
    sub=0
    mul=0
    div=0
    mod=0
    def Add(self,a,b):
       self.add=a+b
    def Sub(self,a,b):
        self.sub=a-b
    def Mul(self,a,b):
        self.mul=a*b
    def Div(self,a,b):
        self.div=a/b
    def Mod(self,a,b):
        self.mod=a%b
    def display(self):
        print("Addition is :",self.add)
        print("Substraction is :",self.sub)
        print("Multiplication is :",self.mul)
        print("Division is :",self.div)
        print("Modulus is :",self.mod)
    
MO=MathematicalOperation()
MO.Add(10,20)
MO.Sub(20,10)
MO.Mul(10,2)
MO.Div(10,5)
MO.Mod(2,10)
MO.display()
