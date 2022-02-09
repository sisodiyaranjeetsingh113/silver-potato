'''
* It contains  key:value formated data..
* we can access all value by it's key...
* we can use any key one time in dictionary but we can change it...
* Ordered : data can be accessing in ordered.
        --- 3.6  ---  unordered
version-
        --- 3.7 ---   ordered
* Duplicacy not allowed 
    *   key can be duplicate
* changable .....

'''

dict1={"id":101,"name":"Ranjeet Singh","salary":15000,"campany":"pythonmate","location":"Indore"}
print("look of dictionary")
print(dict1)
print(" we can can change the value of key..   dictionaryname['key']=anothervalue")
dict1["salary"]=14000
print(dict1)
print("length of dictionary by len(nameofdictionary)")
print(len(dict1))
print("we can get value by dictionaryname.get('key')")
print(dict1.get("name"))
print("we access all keys by dictionaryname.keys()")
print(dict1.keys())
print("we access all values by dictionaryname.values()")
a=dict1.values()
print(a)
dict1['name']="Aryan"
print(a)

print(dict1.items())



'''fuction'''
dict1.update({"fathername": "Rann singh"})
print(dict1)


x=dict1.pop('fathername')
print(x)

x=dict1.popitem()
print(type(x))
print(x)
dict1.clear()
print(dict1)










