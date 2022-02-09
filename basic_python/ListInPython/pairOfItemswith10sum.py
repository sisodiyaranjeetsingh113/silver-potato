LIST=[]
j=0
count=0
for i in range(100) :
    LIST.insert(j,i)
    j+=1
print(LIST)

for x in LIST :
    for y in LIST : 
        if(x<y):
            if(x+y==50) :
                count=count+1
                print((x,y))
        else:
            pass
print(count)            