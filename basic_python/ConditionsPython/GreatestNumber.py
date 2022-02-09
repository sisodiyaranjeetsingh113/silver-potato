'''
find which is greatest number from a,b,c,d

'''
a=20
b=10
c=70
d=600

if (a>b) : 
     if(a>c) :
         if(a>d) :
            print("a is greatest number ")
         else:
            print("d is greatest number")
     elif (c>d):
      print("c is greatest number")
     else :
      print("d is greatest number") 
elif(b>c) :
     if(b>d) :
         print("b is greatest number")
     else :
         print("d is greatest number")
elif(c>d) :  
    print("c is greatest number")    
else:
    print("d is greatest number")





