print('Enter a number : ')
x=int(input())
SUM=0
for i in range(1,21) :
      print(x**i,end=',')
      SUM=(x**i)+SUM
print('Sum of a Series is',SUM)
      