import urllib.request, json 
import pandas as pd

with urllib.request.urlopen("https://bw-interviews.herokuapp.com/data/providers") as url:
    data = json.loads(url.read().decode())
    
output_file = 'outputs/api_data.csv'

df_api = pd.DataFrame.from_records(data['providers'])
df_api.to_csv(output_file,index=None)

print("Saved to: " + output_file)
