
def Area_Of_Circle(radius) :
    Pi=3.14    
    AOC=Pi*(radius**2)
    return AOC

print("Enter a  radius")
r=int(input())
aoc=Area_Of_Circle(r)
print("Area of circle is :",aoc)

def Area_Of_Rect(length,width) :
    AOR=length*width
    return AOR

print("Enter a  length :")
l=int(input())
print("Enter a  width:")
w=int(input())
aor=Area_Of_Rect(l,w)
print("Area of Rect. is :",aor)

def Area_Of_Square(side) :
    AOS=side**2
    return AOS

print("Enter a  side :")
s=int(input())

aos=Area_Of_Square(s)
print("Area of Square is :",aos)

