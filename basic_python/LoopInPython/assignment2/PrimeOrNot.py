print('Enter a number : ')
x=int(input())
count=0
for j in range(2,x) :
    if(x%j==0):
        count=1
if (count==0):
     print(x,'is Prime Number')
else:
    print(x,' is not a Prime Number')