class Cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
       self.ADD=self.a+self.b
    def sub(self):
        self.SUB=self.a-self.b
    def mul(self):
        self.MUL=self.a*self.b
    def div(self):
        self.DIV=self.a/self.b
    def mod(self):
        self.MOD=self.a%self.b
    def display(self):
        print("Addition :",self.ADD)
        print("Substraction :",self.SUB)
        print("Multiplication :",self.MUL)
        print("DIvision :",self.DIV)
        print("Modulus :",self.MOD)
cal=Cal(10,20)
cal.add()
cal.sub()
cal.mul()
cal.div()
cal.mod()
cal.display()