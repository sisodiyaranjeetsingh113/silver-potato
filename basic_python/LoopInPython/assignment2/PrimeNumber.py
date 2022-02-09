
count=0
for i in range(2,51,1) :
    flag=0
    for j in range(2,i,1) :
        
        if(j<i) :
            if(i%j==0) :
                flag=1
                
    if (flag==0) :
        print(i)
        count+=1
print("Total Prime Number :",count)