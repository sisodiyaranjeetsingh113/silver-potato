tp=(2,3,1,6,3,1,3,8,3)
print(tp)
st=set(tp)
print(st)
lt=list(st)
print(lt)
repeatingElement=0
for j in lt:
    count=0    
    for i in tp :
        repeatingElement=j
        if(repeatingElement==i)  :
            count+=1
    if(count>0) :
        print(repeatingElement," is Exists in a tuple ",count," times")
    else:
        print(repeatingElement," is not exists in a tuple..")