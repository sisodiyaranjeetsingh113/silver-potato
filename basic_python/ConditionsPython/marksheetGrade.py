'''
mark =?

o/p 70+  =>dist
60-69    => A
50-59    => B
40-49    => C 
0-40     => Fail
 
'''
x=int(input("Enter a number(0-100) :"))
if(x>=70 and x<=100) :
    print("Dist")
elif(x>=60 and x<=69) :
    print(" Grade A")
elif (x>=50 and x<=59):
    print("Grade B")
elif (x>=40 and x<=49):
    print("Grade C")  
else :
    print(" Fail :)")
 
 
