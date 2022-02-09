import pandas
login={
    "Rakesh sharma":{
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
login_frame=pandas.DataFrame(login)

connections="yes"

while(connections=="yes"):
    
    username=input("User Name :")
    password=input("Password :")
    
    for x in login:
        if(username==login[x]["User Name"] and password==login[x]["Password"]) :
            print("Hey!   ",x," you are our member")
            print("I Find your Email Id",login[x]["Email Id"])
            connections="done"
            break
    if(connections=="done") :
        print("You have login successfully")
    else:
       print("Please check your username and password!!!")
connections=input('''if, Do you want to login again, 
    
    then type    ->   yes       
    otherwise type->   no 
     
     :''')




    