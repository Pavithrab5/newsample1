import pandas as pd
df=pd.read_csv("C:/Users/user696/PycharmProjects/pythonProject3/pokemon_data.csv")
print(df)
#print(df.head(5))
#print(df.tail(6))
df_txt=pd.read_csv("pokemon_data.csv")
#print(df_txt)
#read columns
'''
print(df[["Name","Type 1","HP"]])
#read each row
print(df.iloc[0:4])
for index,row in df.iterrows():
    print(index,row['Name'])
print(df.loc[df['Type 1']=="Grass"])
## Read a specific location (R,C)
print(df.iloc[2,1])

# sort
(df.sort_values(['Speed'], ascending=True)

print(df.sort_values(['Type 1', 'Speed'], ascending=[1,0]))

# changes to data

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

print(df)

# drop a cloumn from df
#df = df.drop(columns=['Total'])
#print(df)

#df['Total'] = df.iloc[:, 4:10].sum(axis=1)

#print(df)
#col_title=["Type 1","Speed"]
#df=df.reindex(col_title)
#print(df)
df['total1']=df['Attack']+df['Defense']+df['Speed']
print(df)
'''
'''
def swap_col(df,c1,c2):
    df['temp']=df[c1]
    df[c1]=df[c2]
    df[c2]=df['temp']
    df.drop(columns=['temp'],inplace=True)
    print(df)
df=swap_col(df,'Name','Type 1')



#swap
df['Type 1'],df['Type 2']=df['Type 2'],df['Type 1']
print(df)


#b=df.columns
#print(b)
a=df.loc[df["Type 1"].str.startswith('A')]
#print(a)
#attack+defence+speed(odd sum)
c=df.iloc[1: :2,[5,6,9]].sum(axis=1)
#print(c)


#dates=pd.date_range('20001118',periods=800)#
#df['#']=dates
#print(df)

df['dates']=pd.date_range('20001118',periods=800)#
df.set_index("dates",inplace=True)
print(df)

'''
df2=df.groupby('Type 1').sum()
print(df2)




