class Area: 
    def __init__(self,length,width,side,radius):
        self.radius=radius
        self.side=side
        self.length=length
        self.width=width
    def AreaOfCircle(self):
        Pi=3.14
        self.areaofcircle=Pi*(self.radius**2)
    def AreaOfRect(self):        
        self.areaofrect=self.length*self.width
    def AreaOfSquare(self):  
        self.areaofsquare=self.side**2

class PaintCost(Area):
    def __init__(self,PCC,PCR,PCS,length,width,side,radius):
        super().__init__(length,width,side,radius)
        self.PCC=PCC
        self.PCR=PCR
        self.PCS=PCS
    def PaintCostForCircle(self):
        print("Area of circle :",self.areaofcircle)
        self.PCCPS=self.areaofcircle*self.PCC
        print("Paint cost for circle per square :",self.PCCPS)
    def PaintCostForRect(self):
        print("Area of rectaingle :",self.areaofrect)
        self.PCRPS=self.areaofrect*self.PCR
        print("Paint cost for Rectaingle per square :",self.PCRPS)
    def PaintCostForSquare(self):
        print("Area of square :",self.areaofsquare)
        self.PCSPS=self.areaofsquare*self.PCS
        print("Paint cost for square per square :",self.PCCPS)

paintCost=PaintCost(50,40,30,10,5,5,10)
paintCost.AreaOfCircle()
paintCost.AreaOfRect()
paintCost.AreaOfSquare()
paintCost.PaintCostForCircle()
paintCost.PaintCostForRect()
paintCost.PaintCostForSquare()
