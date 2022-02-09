import pandas
login={
    "Rakesh Sharma":{
        "User Name":"sharmarakesh123",
        "Password": "rakesh123",
        "Email Id": "rakesh123@gmail.com"
    },
  
    "Kalpana Chawla":{
        "User Name":"chawlakalpana123",
        "Password": "kalpana123",
        "Email Id": "kalpana123@gmail.com"
    },

    "Ranjeet Singh":{
        "User Name":"singhranjeet123",
        "Password": "ranjeet123",
        "Email Id": "ranjeet123@gmail.com"
    },
    "Arjun Singh":{
        
   
        "User Name":"singharjun123",
        "Password": "arjun123",
        "Email Id": "arjun123@gmail.com"
    },
    
    "Aryan Sharma":{
        "User Name":"sharmaaryan123",
        "Password": "aryan123",
        "Email Id": "aryan123@gmail.com"
    }
}

def employee_data(name):
    print("===============================================================================")
    login_frame=pandas.DataFrame(login)  
    print("===============================================================================")
    try:
        Emp_Name=name
        rajeeet_Singh_data=login_frame[[Emp_Name]]
    except:
        print(Emp_Name," doesn't exists.....")
    else:    
        print(rajeeet_Singh_data)
        print("===============================================================================")
    finally:
        print("===========================VISIT AGAIN ==============================================")
name=input("Enter a Employee name:").title()
employee_data(name)

login_data_frame=pandas.Series(login,index=[name])
print(login_data_frame)


