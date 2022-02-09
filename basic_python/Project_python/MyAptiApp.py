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
def simple_interest(p,r,t):
    SI=(p*r*t)/100
    return SI
def return_selling_price():
    s_p=random.randint(100,1000)
    return s_p
def return_cost_price():
    c_p=random.randint(100,1000)
    return c_p
def cal_profit(c_p,s_p):
    c_profit=((s_p-c_p)*100)/c_p
    return c_profit
def cal_loss(c_p,s_p):
    c_loss=((c_p-s_p)*100)/c_p
    return c_loss

connection=True
print(''' Hlw Dear,
                   Welcome to you in my MyAptiApp. You can do prepairation and practice of aptitute
                   questions,There various topic for  you''')
while(connection):
    print("1=> SimpleInterest \n 2=> Profite/Loss \n 3=> EXIT")
    Score=0
    ch=int(input("Enter your Choice:"))
    if(ch==1):
        n=1
        
        
        while(n<=1):
         
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
        profit=0
        loss=0
        
        while(n<=10):
         
            C_P=return_cost_price()
            S_P=return_selling_price()
            if(C_P<S_P):
                profit=int(cal_profit(C_P,S_P))
                occur="profit"
                a=(profit+9)
                b=(profit+5)
                c=(profit)
                d=(profit+3)
                
                

            else:
                loss=int(cal_loss(C_P,S_P)) 
                occur="loss"
                a=(loss+5)
                b=(loss+2)
                c=(loss)
                d=(loss+3)
                

            print('''Q.no.''',n,'''Find gain or loss per cent ?. when 
            Cost Price=''',C_P,'''\n             Selling Price =''',S_P,'''\n''')
            
                
            

                

            List=[a,b,c,d]
            random.shuffle(List)
            

            print(''' 1.%.1f'''%List[0],'''\n\n2.%.1f'''%List[1],'''\n\n3.%.1f'''%List[2],'''\n\n4.%.1f'''%List[3],'''\n\n''')
            Answer=input("Type Answer here:")
            
            loss=str(float(loss))
            profit=str(float(profit))
            print(loss)
            print(profit)
            print(Answer)
            if(Answer==loss or Answer==profit):
                Score=Score+2
            else:
                pass
            n=n+1
        print('''Right:''',(Score/2),'''\nWrong:''',10-(Score/2),'''\n\nYou are score''',Score)                           
    if(ch>=4):
        print("------------------------------thanks for Visit-------------------------------------------------")
        break    

           
       
