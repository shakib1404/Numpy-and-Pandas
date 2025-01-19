import pandas as pd

dataset={
    'cars':["bmw","audi","nice"],
    'passings':[3,7,2]
    
}

myvar=pd.DataFrame(dataset)
print(myvar)

a=[3,5,7]
myv2=pd.Series(a)
print(myv2)
print(myv2[0])
myv3=pd.Series(a,index=["x","y","z"])
print(myv3)
print(myv3["y"])
calories={"day1":420, "day2":450, "day3":550}
myv4=pd.Series(calories,index=["day1","day2"])
print(myv4)