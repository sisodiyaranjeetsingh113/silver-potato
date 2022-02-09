'''
1
13
135
1357

Odd number traingle

'''
for i in range(1,8) :
    for j in range(1,i+1) :
        if(j%2!=0 and i%2==1) :
          print(j,end=" ")
    print()  