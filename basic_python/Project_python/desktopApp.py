import random
def return_principle():
    P=random.randint(1000,5000)
    return P
def return_rate():
    R=random.randint(5,10)
    return R
def return_time():
    T=random.randint(2,12)
    return T
def return_simple_interest(p):
    
    start=int(p/10)
    end=int(p/5)
    if(p<=10):
        start=int(p*100)
        end=int(p*500)

    SI=random.randint(start,end)
    return SI
def simple_interest(p,r,t):
    SI=(p*r*t)/100
    return SI
def rate_of_interest(p,t,si):
    r=(si*100)/p*t
    return r
def principal_amount(R,T,SI):
    P=(SI*100)/R*T
    return P

connection=True
print(''' Hlw Dear,
                   Welcome to you in my MyAptiApp. You can do prepairation and practice of aptitute
                   questions,There various topic for  you''')
while(connection):
    print("1=> SimpleInterest \n 2=> RateOfInterest \n 3=> PrincipalAmount \n 4=> EXIT")
    Score=0
    ch=int(input("Enter your Choice:"))
    if(ch==1):
        n=1
        
        
        while(n<=10):
         
            P=return_principle()
            R=return_rate()
            T=return_time()
            SI=simple_interest(P,R,T)
            print('''Q.no.''',n,'''  A sum of''',P,'''Rs is deposited into SBI Bank for''',T,'''years. if the bank 
            is Providing ''',R,'''%'''+'''rate then find simple interest?\n''')
            a=SI+19
            b=SI+15
            c=SI
            d=SI+13
            List=[a,b,c,d]
            random.shuffle(List)
            

            print(''' 1.''',List[0],'''\n\n2.''',List[1],'''\n\n3.''',List[2],'''\n\n4.''',List[3],'''\n\n''')
            Answer=input("Type Answer here:")
            
            SI1=str(SI)
            if(Answer==SI1):
                Score=Score+2
            else:
                pass
            n=n+1
        print('''Right:''',(Score/2),'''\nWrong:''',10-(Score/2),'''\n\nYou are score''',Score)  
    if(ch==2):
        n=1
        while(n<=10):
         
            P=return_principle()
            SI=return_simple_interest(P)
            T=return_time()
            R=rate_of_interest(P,T,SI)
            print('''Q.no.''',n,'''  A sum of''',P,'''Rs amount to''',SI,''' in''',T,'''years at the rate of
            simple interest. What is the rate of interest?\n''') 
            a=R
            b=R+1
            c=R+3
            d=R+7
            List=[a,b,c,d]
            random.shuffle(List)
            print(''' 1. %.2f'''%List[0],'''\n\n2.  %.2f'''%List[1],'''\n\n3.  %.2f'''%List[2],'''\n\n4.  %.2f'''%List[3],'''\n\n''')
            Answer=input("Type Answer here:")
            
            R1=str(R)
            

            if(Answer==R1):
                Score=Score+2
            else:
                pass
            n=n+1
        print('''Right:''',(Score/2),'''\nWrong:''',10-(Score/2),'''\n\nYou are score''',Score)
    if(ch==3):
        n=1
        while(n<=10):
         
            R=return_rate()
            SI=return_simple_interest(R)
            T=return_time()
            P1=principal_amount(R,T,SI)
            print('''Q.no.''',n,'''  Find the Principal which will amonut to''',SI,''' in''',T,'''years 
            at''',R,'''%'''+''' rate of interest?\n''') 
            P=int(P1)
            a=P
            b=P+100
            c=P+300
            d=P+700
            List=[a,b,c,d]
            random.shuffle(List)
            print(''' 1. %d'''%List[0],'''\n\n2.  %d'''%List[1],'''\n\n3.  %d'''%List[2],'''\n\n4.  %d'''%List[3],'''\n\n''')
            Answer=input("Type Answer here:")
            
            P1=str(P)
            
            
            if(Answer==P1):
                Score=Score+2
            else:
                pass
            n=n+1
        print('''Right:''',(Score/2),'''\nWrong:''',10-(Score/2),'''\n\nYou are score''',Score)                        
    if(ch>=4):
        print("------------------------------thanks for Visit-------------------------------------------------")
        break    

           
       
