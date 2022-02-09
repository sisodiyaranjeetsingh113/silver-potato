"""operation of list  =>
sort()
reverse()
copy()
"""
list1=[1,12,2,9,3,10,4,5,13,6,14,7,11,8,15]
list1.sort()
print(list1)
list1.reverse() 
print(list1)
list2=list1.copy()

list1.insert(3,30)
print(list1)
print(list2)

