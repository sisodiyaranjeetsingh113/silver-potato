class Area:
     
     def __init__(self,r):      
        self.radius=r
        self.side=self.length=int(input("Enter a length or side :"))
        self.width=int(input('Enter a width :'))
    def AreaOfCircle(self):
        Pi=3.14
        self.areaofcircle=Pi*(self.radius**2)
    def AreaOfRect(self):        
        self.areaofrect=self.length*self.width
    def AreaOfSquare(self):  
        self.areaofsquare=self.side**2

class PaintCost:      
        PCC=50
        PCR=40
        PCS=30

class Display(Area,PaintCost):
    def __init__(self,radius):
        super().__init__(radius)        
    def PaintCostForCircle(self):
        print("------------------------------------------------")
        print("Area of circle :",self.areaofcircle)     
        self.PCCPS=self.areaofcircle*self.PCC
        print("Paint cost for circle per square :",self.PCCPS)         
    def PaintCostForRect(self):
        print("------------------------------------------------")
        print("Area of rectaingle :",self.areaofrect)
        self.PCRPS=self.areaofrect*self.PCR
        print("Paint cost for Rectaingle per square :",self.PCRPS)            
    def PaintCostForSquare(self): 
        print("------------------------------------------------")
        print("Area of square :",self.areaofsquare)
        self.PCSPS=self.areaofsquare*self.PCS
        print("Paint cost for square per square :",self.PCCPS)
        print("------------------------------------------------")

r=int(input("Enter a radius :"))
obj_display=Display(r)
obj_display.AreaOfCircle()
obj_display.AreaOfRect()
obj_display.AreaOfSquare()
obj_display.PaintCostForCircle()
obj_display.PaintCostForRect()
obj_display.PaintCostForSquare()

 