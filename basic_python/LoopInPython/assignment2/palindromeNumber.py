print('Enter a number :')
x=int(input())
farwardNumber=x
reverseNumber=0
while(x>0) :
   remainder=x%10
   reverseNumber=(reverseNumber*10)+remainder
   x=x//10       
if(farwardNumber==reverseNumber) :
    print(farwardNumber,"is palindrome number")
else:
    print(farwardNumber,"is not a palindrome number")
