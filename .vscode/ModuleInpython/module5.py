import module1 as m1
from module1 import sub,A
def mul(a,b):
    c=a*b
    print("mul is :",c)


mul(10,5)


a=m1.add(10,30)
print("sum is:",a)
a=sub(10,30)
print("sub is:",a)

print("name :",m1.login["Rakesh sharma"]["User Name"])


class B(A):
    def test(self):
        print("this is test from class B")

obj=B()
obj.test()
obj1=A()
obj1.demo()
