import numpy as np
import pandas as pd
'''
#using pandas series is used to print the data in column type one by one,[one dimensional array] and it also defines the dtype
a=[1,6,7]
ser=pd.Series(a)
print(ser)
var=pd.Series(a,index=[10,20,30])
#print(var)#labels-it can be used to access a specified value ,similar to our indexes
#we can also locate rows in dataframes
#comma seperated files
#read_csv is used to read the custom document

df=pd.read_csv('Pandas_Basics_Data.txt')
print(df)

mydataset={'bikes':["honda","scooty","splender"],"meilage":[30,40,50]}
mydata=pd.DataFrame(mydataset)
#print(mydata)
#print(mydata.loc[0])
#print(mydata.loc[[0,1]])
#loc-locate is used to print only required things :compare the above two for more understanding
#to check the version of the pandas we can use_version
#print(pd.__version__)

#inder_changer-we can also change the index values
index_change=pd.DataFrame(mydataset,index=['b1','b2','b3'])
#print(index_change)
print('---------------------')
#print(index_change.loc['b2'])
#head & tail
#print(df.head(1))
#print(df.tail(2))
#print(df.index)#RangeIndex(start=0, stop=3, step=1)
#print(df.columns)# col names-Index(['pavithra', 'divya', 'jagan', 'rupa'], dtype='object'
#print(df.to_numpy())
#print(df.describe())#all contents in the the array
print(df.info())

a=pd.Series([1,3,5,np.nan,6,8])
print(a)
print(a[0])
print('---------------------')
'''
#dates=pd.date_range('20190706',periods=5)#periods =rows
dates=pd.date_range('20001118',periods=5)#year_month_date
#print(dates)
#random float values
df=pd.DataFrame(np.random.randn(5,4),index=dates,columns=list("ABCD"))#2D array starting values should be given as 1st parameter as 5 that is periods values#4 cols
print(df)

df2=pd.DataFrame(
    {
        "A":1.0,
        "B":pd.Timestamp("20130211"),
        "C":pd.Series(1,index=list(range(4)),dtype="float32"),
        "D":pd.array([3]*4,dtype="int32"),
        "E":pd.Categorical(["tested","trained","tested","trained"]),
        "F":"Fool"
    }
)
#print(df2)
#print(df2.dtypes)
#print((df2.tail(2)))
#print("---------")
#print(df2.head(2))
print("-----------")
#print(df2.describe())
#print(df2.T)
#sorting
#print(df.sort_index(axis=0,ascending=True))
#print(df.sort_index(axis=0,ascending=False))
'''
#getting values
print(df["A"])
print(df.A)
print(df.B)
'''
#slicing with data frames
print(df[0:3])
#selection -loc()




























