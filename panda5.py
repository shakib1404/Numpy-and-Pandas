

import pandas as pd

df = pd.read_csv(r'C:\Users\ASUS\Downloads\fixed_cleaned_data.csv')


for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df.to_string())
