import pandas as pd
data={'Name':['Alice','Jacob','Bob'],
      'Age':[25,33,43],
      'country':["USA","Canada","UK"]


}

my_data=pd.DataFrame(data)
print(my_data)


#loading data frame
df=pd.read_excel("my_excel.xlsx")
df=pd.read_csv("read.csv")
df=pd.DataFrame(data)# making up my own data frame 