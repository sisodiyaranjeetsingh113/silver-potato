import os
'''
fname="baba.txt"  
f=open(fname,"w")
f.write("Ohh!! world")
print("file is created.....!!!")
f.close()
os.remove("baba.txt")'''

''''
fname="baba.txt"  
f=open(fname,"a")
f.write("Yup!! world")
print("file is created.....!!!")
f.close()
'''
'''
fname="baba.txt"  
f=open(fname,"r")

f.seek(6)
print(f.readline())
print(f.readline())

print("file is created.....!!!")
f.close()


'''
fname="baba1.txt"  
f=open(fname,"x")

f.seek(6)
print(f.write("yes"))
print(f.write("boss"))

print("file is created.....!!!")
f.close()

