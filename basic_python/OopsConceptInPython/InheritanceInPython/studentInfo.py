class  studentdata():
    def __init__(self):
        self.student_data={
            "1001":{
                "student_name":"Ranjeet Singh",
                "date_of_birth":"8/9/2005",
                "science":90,
                "social_science":80,
                "mathematics":75,
                "hindi":95,
                "english":70,
                "sanskrit":80
            },
            "1002":{
                "student_name":"aryan choudary",
                "date_of_birth":"1/1/2005",
                "science":90,
                "social_science":60,
                "mathematics":75,
                "hindi":55,
                "english":60,
                "sanskrit":80
            },
            "1003":{
                "student_name":"pankaj vyas",
                "date_of_birth":"14/1/2005",
                "science":80,
                "social_science":80,
                "mathematics":75,
                "hindi":90,
                "english":70,
                "sanskrit":60
            },
            "1004":{
                "student_name":"piyush raghuvanshi",
                "date_of_birth":"1/1/2005",
                "science":85,
                "social_science":80,
                "mathematics":65,
                "hindi":95,
                "english":80,
                "sanskrit":50
            },
            "1005":{
            "student_name":"kamal sharma",
            "date_of_birth":"1/2/2005",
            "science":90,
            "social_science":80,
            "mathematics":75,
            "hindi":95,
            "english":70,
            "sanskrit":80
            },
            "1006":{
            "student_name":"anis hussain",
            "date_of_birth":"12/1/2005",
            "science":90,
            "social_science":80,
            "mathematics":75,
            "hindi":95,
            "english":70,
            "sanskrit":80
            }
        }
        
    def get_student_data(self):
        return self.student_data
class result(studentdata):
    def __init__(self,roll_number):
        self.status=False
        self.roll_number=roll_number
        super().__init__()
        self.s_d=self.get_student_data()
        for x in self.s_d:
            if(self.roll_number==x):
                print("Hlw ",self.s_d[x]["student_name"])
                print("----------------------------------------------------------------------------------------------------") 
                self.status=True
                break
            else:                
                self.status=False
                
    def Done(self):
        return self.status
print("-------------------------------------------------------")
print("----------------------Welcome to you-------------------")
n="yes"

while(n!="no"):
    
    print("-------------------------------------------------------")
    r=input("Enter your roll number :")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    
    result_obj=result(r)
    popup=result_obj.Done()
    if(popup):
        print("                             BOARD OF SECONDARY EDUCATION, MADHYA PRADESH,BHOPAL \n")
        print("                                    HIGH SCHOOL CERTIFICATE EXAMINATION 2021    \n") 
        s_d=result_obj.get_student_data()
        for y in s_d:
            if(y==r):
                print(" ROLL NUMBER :",y,"\n")
                print(" STUDENT NAME :",s_d[y]["student_name"],"\n")
                print(" SCHOOL NAME : GOVT. HIGHER SECONDARY SCHOOL INDORE \n")
                print(" STUDENT CLASS : 10th  \n")
                print(" STUDENT STATUS : REGULAR \n")
                print("----------------------------------------------------------------------------------------------------")
                print("SUBJECT NAME                  SUBJECT MARKS \n")
                print("Science                          ",s_d[y]["science"])
                print("Social Science                   ",s_d[y]["social_science"])
                print("Mathematics                      ",s_d[y]["mathematics"])
                print("Hindi                            ",s_d[y]["hindi"])
                print("English                          ",s_d[y]["english"])
                print("Sanskrit                         ",s_d[y]["sanskrit"])

                x=(s_d[y]["science"]+s_d[y]["social_science"]+s_d[y]["mathematics"]+s_d[y]["hindi"]+s_d[y]["english"]+s_d[y]["sanskrit"])/6
                if(x<=100 and x>=40):
                    Result="Pass"
                    if(x>=70 and x<=100) :
                        Grade="Dist"
                    elif(x>=60 and x<=69) :
                        Grade="A"
                    elif (x>=50 and x<=59):
                        Grade= "B"
                    elif (x>=40 and x<=49):
                        Grade="C" 
                else :
                    Grade="F"
                    Result="Fail"
        print("----------------------------------------------------------------------------------------------------")    
        print("Percentage                        ",x)         
        print("Grade                             ",Grade)
        print("Result Status                     ",Result)

        print("----------------------------------------------------------------------------------------------------") 
        
       
    else:
        print("Please enter correct roll number! \n")
        
    
    
    n=input("Do want to visit again: \n Type (yes/no) :")

    
else:
  print("----------------------------thank for visit---------------------------------")
