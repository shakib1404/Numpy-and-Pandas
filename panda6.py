import pandas as pd

df = pd.read_csv('data10.csv')

print(df.corr())
