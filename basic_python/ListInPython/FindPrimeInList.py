list=[1,2,3,4,5,6,7,8,9,10]
print(list)
count=0
for i in list:
   if(i>1) :
        flag=0
        for j in range(2,i,1) :
            
            if(j<i) :
                if(i%j==0) :
                    flag=1
        if (flag==0) :
        
            print(i)
            count+=1
print("Total Prime Number :",count)