import pandas as pd
csv_file=pd.read_csv('login.csv')
print("===============================================")
print(csv_file.head(1))
print("===============================================")
print(csv_file.info())
print("===============================================")