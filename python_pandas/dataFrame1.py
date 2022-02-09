import pandas as pd
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
}
login_frame = pd.DataFrame(login)
print("==================================================")
print(login_frame)
print("==================================================")
print(login_frame["Ranjeet Singh"])                        #select column of emmloyee 
print("==================================================")
print(login_frame.loc["User Name"])
print("==================================================")
print(login_frame.loc[["User Name","Password"]])   #select row whose we need
print("==================================================")