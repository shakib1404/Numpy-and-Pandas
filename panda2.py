import pandas as pd

# Load the DataFrame
df = pd.read_csv('./data3.csv')

# Replace common placeholders with proper missing value representations
df.replace(['NaN', 'null', '', None], pd.NA, inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)
print("Cleaned DataFrame after dropna():")
print(df.to_string())

# Reset the DataFrame (for demonstration)
df = pd.read_csv('./data3.csv')
df.replace(['NaN', 'null', '', None], pd.NA, inplace=True)

# Fill missing values with 130
df.fillna(130, inplace=True)
print("After fillna(130):")
print(df.to_string())
print("NaN Counts:", df.isna().sum())
x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True) 


x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True) 
