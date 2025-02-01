import pandas as pd

df = pd.read_csv('data4.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())