print('Enter a number :')
x=int(input())
reverseNumber=0
while(x>0) :
   remainder=x%10
   reverseNumber=(reverseNumber*10)+remainder
   x=x//10     
print(reverseNumber)