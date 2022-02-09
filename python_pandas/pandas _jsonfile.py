import pandas as pd

json_file=pd.read_json('login.json')

print(json_file.to_string())