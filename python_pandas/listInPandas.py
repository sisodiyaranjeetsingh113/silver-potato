import pandas as pd
fruit_list=["banana","mango","papaya","greps","apple","orange","water melon"]
fruit_data_frame=pd.DataFrame(fruit_list)
print("=============================================")
print(fruit_data_frame)          #to print managing data frame
print("=============================================")
print(fruit_data_frame[4:6])                    # list slicing
print("=============================================")
fruit_data_frame=pd.Series(fruit_list)
print(fruit_data_frame[0])                      #print element with index
print("=============================================")
#myvar = pd.Series(a, index = ["x", "y", "z"]) #it can give index name as we want 
fruit_data_frame=pd.Series(fruit_list,index=["b","m","p","g","a","o","wm"])  
print(fruit_data_frame)
print("=============================================")
print(fruit_data_frame["b"])             #value access by it 
print("=============================================")