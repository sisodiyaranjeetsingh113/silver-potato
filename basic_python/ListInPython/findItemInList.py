j=0
lst=[]
for  i  in range(1,21,1) :
    lst.insert(j,i)
    j+=1
     
print(lst)  
Here=False
LookAtHere=int(input("Enter a number to be find    :"))
for InHere in lst :
    if(LookAtHere==InHere) :
         Here=True
if(Here==True) :
    print(LookAtHere," is Exists in a list...")
else :
    print(LookAtHere," is not Exists in a list")