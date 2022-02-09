from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def rate_of_interest(self):
        pass

class CarLoan(Bank):
    def __init__(self,id):
         self.id=id
    def get_car_loan_info(self):
        self.popup=False  
        self.carloan={ 
            "101":{
            "loan_holder":"Shivam Patidar",
            "bank_name":"Bank of Baroda",
            "bank_status":"Government",
            "loan_price":1000000,
            "duration":5,
            "payment_per_year":12,
            "interest":362500.0
            },
            "102":{
            "loan_holder":"Aryan Choudhary",
            "bank_name":"Punjab & Sind Bank",    
            "bank_status":"Government",
            "loan_price":1000000,
            "payment_per_year":12,
            "interest":350000.0,
            "duration":5
            },
            "103":{
            "loan_holder":"Rohit Sen",  
            "bank_name":"Central Bank",    
            "bank_status":"Govrnment",
            "loan_price":1000000,
            "interest":362500.0,
            "payment_per_year":12,
            "duration":5
            },
            "104":{
            "loan_holder":"Taresh Ayuspure",
            "bank_name":"Canara Bank",
            "bank_status":"Government",
            "loan_price":1000000,
            "interest":365000.0,
            "duration":5,
            "payment_per_year":12
            
            },
            "105":{
            "loan_holder":"Gaurishankar Sahu",
            "bank_name":"Punjab National Bank",
            "bank_status":"Government",
            "loan_price":1000000,
            "duration":5,
            "interest":365000.0,
            "payment_per_year":12
            }                     
        }  
        return self.carloan

    def get_popup(self,c_l_info):
        self.c_l_info=c_l_info
        for x in self.c_l_info:
            if(self.id==x):
               self.popup=True
               break
                   
        return self.popup
    def rate_of_interest(self,p,i,t):
        self.loan_price=p
        self.interest=i
        self.time=t
        self.r_o_interest=(self.interest*100)/(self.loan_price*self.time)
        return self.r_o_interest
    def get_emi(self,ppy):
        self.ppy=ppy
        self.emi=(self.interest+self.loan_price)/(self.ppy*self.time)
        return self.emi

    
print("-------------------------------------------------------")
print("----------Welcome to you loan website-------------------")
n="yes"

while(n!="no"):
    
    print("-------------------------------------------------------")
    id=input("Enter your Loan registration id :")
    print("----------------------------------------------------------------")
    print("THIS IS A PLACE TO GIVE CAR LOAN TO THE NEEDY CUSTOMER \n             FROM GOVERNMENT BANK... ")
    print("----------------------------------------------------------------")
    
    carloan_obj=CarLoan(id)
    c_l_i=carloan_obj.get_car_loan_info()
    popup=carloan_obj.get_popup(c_l_i)
    if(popup):
        for y in c_l_i:
            if(y==id):
                print(y,"\n")
                print("CUSTOMER NAME         :",c_l_i[y]["loan_holder"],"\n")
                print("BANK NAME             :",c_l_i[y]["bank_name"],"\n")
                print("BANK STATUS           :",c_l_i[y]["bank_status"],"\n")
                print("LOAN PRICE            :",c_l_i[y]["loan_price"],"\n")
                print("DURATION (loan term)  :",c_l_i[y]["duration"],"year..\n")
                print("PAYMENT PER YEAR      : ",c_l_i[y]["payment_per_year"]," times....\n")
                print("INTEREST              :",c_l_i[y]["interest"],"\n")
                print("----------------------------------------------------------------------------------------------------")
                
                print("----------------------------------------------------------------------------------------------------")    
                p=c_l_i[y]["loan_price"]
                i=c_l_i[y]["interest"]
                t=c_l_i[y]["duration"]
                print("Rate of Interest                        :",carloan_obj.rate_of_interest(p,i,t),"%\n")         
                print("----------------------------------------------------------------------------------------------------\n")
                ppy=c_l_i[y]["payment_per_year"]
                print ("EMI (monthly installment)              :",carloan_obj.get_emi(ppy),"per month only")
                print("----------------------------------------------------------------------------------------------------")
                print("----------------------------------------------------------------------------------------------------") 
        
       
    else:
        print("Please enter correct loan holder id!!!! \n")
        
    
    
    n=input("Do want to visit again! \n Type (yes/no) :")

    
else:
  print("----------------------------thank for visit---------------------------------")


    


