import module1

def mul(a,b):
    c=a*b
    print("mul is :",c)


mul(10,5)


a=module1.add(10,30)
print("sum is:",a)
a=module1.sub(10,30)
print("sub is:",a)

print("""Rakesh Sharma Detail =>
""",module1.login["Rakesh sharma"])