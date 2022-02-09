    
def Factorial(number) :
    i=1
    while(number>0) :
         i=i*number
         number-=1
    return i
Number=int(input("Enter a number to be factorial"))
Fact=Factorial(Number)
print("Factorial of a",Number,"is :",Fact)