import pandas as pd
import numpy as np
import requests

excel_file = 'Org_sample_data.xlsx'
new_excel = 'New_sample_data.xlsx'

df = pd.read_excel(excel_file)
df1 = pd.read_excel(new_excel)

payload = {'q': 'Miami, USA', 'units': 'imperial'}

headers = {'x-rapidapi-key': MYKEY}

url = 'https://community-open-weather-map.p.rapidapi.com/weather?'

r = requests.get(url, params=payload, headers = headers)

# print(r.json()['main']['temp'])

df = pd.read_json(r.content,typ='series')