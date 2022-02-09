
print("""
Integer in defferent defferent format

****Decimal :- In python by default decimal

****Binary :- numbes is lying in between (0 to 1)


****Octal  :- numbers is lying in between (0 to 7)

****Hexadecimal :- numbers is lying in between (0 to 9 and A to F)

 """)
a=1111
print(a)
print(type(a))


a=0b1111
print(a)
print(type(a))

a=0o156
print(a)
print(type(a))

a=0x1234abc
print(a)
print(type(a))

print("""
Variable Conversion  :-

***For binary conversion  bin()

***For octal conversion    oct()

***For Hexadecimal convertion  hex()
""")
a=bin(15)
print(a)

a= oct(598)
print(a)

a=hex(10)
print(a)
