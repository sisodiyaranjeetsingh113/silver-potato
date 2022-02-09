'''
Tuple:-> tuple is a  hetrogeneous collection of  data 
1. Unchangable...
2.Duplicacy allow...
2. Ordered.....
tp=(10,30,50,30)

tp[0]=1000  not support item assignment... means (Unchangable)



tp=(10,30,50,30)
print(tp)
print("length :",len(tp))

tp=(200)
print(type(tp))      #<class 'int'>

#if i want to make a tuple with one element then

tp=(200,)
print(type(tp))    #<class 'tuple'>

tp=()

print(type(tp)) 

del tp           #we can delete tuple but not tuple element like del tp[0]
print(tp)

tp=(200,True,4.5,"cnc",10,56)
print(tp[2:])    # 4.5,'cnc',10,56
print(tp[2:4])   # 200,True,4.5,"cnc"
print(tp[-2:-4]) # ()
print(tp[-4:-2]) #4.5,'cnc'


tp=(200,True,4.5,"cnc",10,56)
lst=[]
j=0
for i in range(0,len(tp)) :
    lst.insert(j,tp[i])
    j+=1
print(lst)

lst.append(100)

tp=tuple(lst)
print(tp)



lst=[]
j=0
for i in range(0,len(tp)) :
    lst.insert(j,tp[i])
    j+=1


lst.remove(100)

tp=tuple(lst)
print(tp)

'''
