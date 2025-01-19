import pandas as pd

dataset={
    'cars':["bmw","audi","nice"],
    'passings':[3,7,2]
    
}

myvar=pd.DataFrame(dataset)
print(myvar)
print(myvar.loc[0])
print(myvar.loc[0:1])

a=[3,5,7]
myv2=pd.Series(a)
print(myv2)

print(myv2.loc[0])
myv3=pd.Series(a,index=["x","y","z"])
print(myv3)
print(myv3["y"])
calories={"day1":420, "day2":450, "day3":550}
myv4=pd.Series(calories,index=["day1","day2"])
print(myv4)
df=pd.read_csv('data.csv')
print(df)
print(df.head(10)) 
df2=pd.read_csv('data2.csv')
print(df2.to_string())
print(pd.options.display.max_rows) 
df3=pd.read_json('data.json')
print(df3.to_string())
print(df.tail()) 