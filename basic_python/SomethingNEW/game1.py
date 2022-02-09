def draw():
    list=
    for i in range(0,10):
        for j in range(0,10):
            if((i==0  or j==0) or (i==9  or j==9)) :
               print("#",end=" ")
            else :
                print(" ",end=" ")
        print(" ")
draw()
