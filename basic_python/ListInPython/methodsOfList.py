'''
insert method
append method
extend method
remove method
pop method
clear method     

del list[0] delete the )index element
del list then it delete entire list...

'''

lst=[1,2,3,4,5,6]
print('''#insert(index,valueOfElement) insert can add a new element in specific index''')
lst.insert(4,6) 
print(lst)
print('''#append(valueOfelement) add a element at the end of list..''')
lst.append(100) 
print(lst)
print('''#extend(anotherlist) add another list at the end of existing list....''')
lst1=["green","red","yellow"]
lst.extend(lst1) 
print(lst)
print('''#remove(specific_element) it remove specific element into the list...... if element not in a list or not passes at calling time then interpreter gives error''')
lst.remove(6)
print(lst)
print('''#pop(index) it remove the specific index element if we don't give an index then it remove element from
 last index into the list ''')
lst.pop()
print(lst)
lst.pop(1) 
print(lst)
print(''' clear() methed clear a list element after then the list look like empty list ->[]''')
lst.clear()
print(lst)