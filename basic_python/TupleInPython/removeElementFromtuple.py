tp=(200,True,4.5,"cnc",10,56,100)
print(tp)
lst=[]
j=0
for i in range(0,len(tp)) :
    lst.insert(j,tp[i])
    j+=1
lst.remove(100)
tp=tuple(lst)
print(tp) 
