print('Enter a number : ')
x=int(input())
X=x

for i in range(x-1,0,-1):
    X=X*i
print('Factorial of ',x,'is :',X)    