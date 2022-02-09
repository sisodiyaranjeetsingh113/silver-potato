
for j in range(1,1000) :
    k=0
    for i in range(1,j) :
        if(j%i==0) :
            k+=i
        
    if(k==j) :
        print(j,"perfect number")