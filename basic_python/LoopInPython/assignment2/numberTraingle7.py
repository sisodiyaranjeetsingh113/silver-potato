print(''' 
    * 
   * *
  * * *
 * * * *
  * * *
   * *
    *
''')



a=' '
for i in range(1,5) :
    for j in range(1,i+1) :
        if(j==1):
          print((4-i)*a,"*",end=' ')
        else:
            print("*",end=' ')
    print()

for i in range(3,0,-1) :
    for j in range(1,i+1,1) : 
        if (j==1) :
            print((4-i)*a,"*",end=' ')
        else :
            print("*",end=' ')
    print()