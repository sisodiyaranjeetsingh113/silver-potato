class Cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        try:
            self.SUM=self.a+self.b
            
        except:
            raise
        else:
            print(self.SUM)

    def sub(self):
        try:
            self.SUB=self.a-self.b            
        except:
            raise
        else:
            print(self.SUB)
    def mul(self):
        try:
            self.MUL=self.a*self.b
            
        except:
            raise
        else:
            print(self.MUL)
    def div(self):
        try:
            self.DIV=self.a/self.b
        except Exception as e:
            print(e)      
        else:
            print(self.DIV)

cal_obj=Cal(10,0)
cal_obj.add()
cal_obj.sub()
cal_obj.mul()
cal_obj.div()

