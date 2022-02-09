class Area:
    def A_Circle(self,r):
        self.Radius=r
        self.a_circle=3.14*self.Radius*self.Radius
    def A_Rect(self,L,B):
        self.B=B
        self.L=L
        self.a_rect=self.L*self.B
    def A_Square(self,Side):
        self.Side=Side
        self.a_square=self.Side*self.Side

class PaintCost(Area):
    def __init__(self,p_circle,p_rect,p_square):
        self.p_circle=p_circle
        self.p_rect=p_rect
        self.p_square=p_square
    def P_Circle(self):
        self.t_p_circle=self.a_circle*self.p_circle
        print("Area of circle : ",self.a_circle)
        print("Total Paint cost for Circle :",self.t_p_circle)
    def P_Rect(self):
        self.t_p_rect=self.a_rect*self.p_rect
        print("Area of rectaigle : ",self.a_rect)
        print("Total Paint cost for Rectaigle :",self.t_p_rect)
    def P_Square(self):        
        self.t_p_square=self.a_square*self.p_square
        print("Area of square : ",self.a_square)
        print("Total Paint cost for Square :",self.t_p_square)
print("-------------------------------------------------------")
print("----------------------Welcome to you-------------------")
n=1
while(n!=0):
    print("-------------------------------------------------------")
    n=int(input("Enter a choice(1 to 4) : \n1   => Circle  \n2   => Rectainlge  \n3   => Square  \n4   => Exit  \n-------------------------------------------------------\nType here   :"))
    
    if(n==1):
        r=int(input("Enter a radius :"))
        p_c=int(input("Enter a paint cost :"))
        p_r=0
        p_s=0
        paintcost=PaintCost(p_c,p_r,p_s)
        paintcost.A_Circle(r)
        paintcost.P_Circle()
    elif(n==2):
        l=int(input("enter a length :"))
        b=int(input("enter a breath :"))
        p_r=int(input("Enter a paint cost :"))
        p_c=0
        p_s=0
        paintcost=PaintCost(p_c,p_r,p_s)
        paintcost.A_Rect(l,b)
        paintcost.P_Rect()
    elif(n==3):
        s=int(input("enter a Side :"))
        p_s=int(input("Enter a paint cost :"))
        p_c=0
        p_r=0
        paintcost=PaintCost(p_c,p_r,p_s)
        paintcost.A_Square(s)
        paintcost.P_Square()
    else:
        n=0
        print("-------------------------------------------------------")
        print("-----------------------Thank you-----------------------")
        print("------------------------------------------------------- \n \n")
else:

    print("----------------------------Visit Again---------------------------------")
        


