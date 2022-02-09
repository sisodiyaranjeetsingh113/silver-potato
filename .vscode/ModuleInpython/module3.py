import module1 as m1
from module1 import sub,add
def mul(a,b):
    c=a*b
    print("mul is :",c)


mul(10,5)


a=add(10,30)
print("sum is:",a)
a=sub(10,30)
print("sub is:",a)

print("name :",m1.login["Rakesh sharma"]["User Name"])