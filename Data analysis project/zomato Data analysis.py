#ZOMATO DATA ANALYSIS PROJECT:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#CREATE THE DATAFRAME:
dataframe=pd.read_csv("Zomato data .csv")

#CONVERT THE DATA TYPE RATING COLUMN:
def handleRate(value):
    if pd.isna(value):
        return value
    value = str(value).split('/')
    return value[0]

dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe['rate'])

#INFO FUNCTION
print(dataframe.info())
#CHECK NULL VALUE:
print(dataframe.isnull().sum())

# Q1: What type of resturant do the majority of customers from orders home:
sns.countplot(x=dataframe["listed_in(type)"])
plt.xlabel("Type of Resturant")
plt.show()
#CONCLUSION:  MAJORITY OF THE RESTURANT FALLS IN DINNING CATEGORY:
print(dataframe.head())

# Q2: HOW MANY VOTES HAS EACH TYPE OF RESTURANT RECEIVE FROM CUSTOMERS:
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result=pd.DataFrame({'votes':grouped_data})
plt.plot(result,c='g',marker="o")
plt.xlabel("Type of Resturant",color="r",size=15)
plt.ylabel("Votes",color="r",size=15)
plt.show()
# CONCLUSION:DINNING RESTURANT HAS RECIEVE MAXIMUM VOTES:
print(dataframe.head())

# Q3: WHAT ARE THE ARE THE RATING THAT THE MAJORITY OF THE RESTURANT HAS RECIEVED:
plt.hist(dataframe['rate'],edgecolor="r")
plt.title("Rating Distribution")
plt.show()
# CONCLUSION: THE MAJORITY RESTURANT RECIEVED RATINGS FROM 3.5 TO 4
print(dataframe.head())

# Q4: ZOMATO HAS OBSERVED THAT MOST COUPLES ORDER MOST OF THEIR FOOD ONLINE. WHAT IS THEIR AVERAGE SPENDING ON EACH ORDERS:
couple_data=dataframe["approx_cost(for two people)"]
sns.countplot(x=couple_data)
plt.show()

#CONCLUSION: THE MAJORIITY OF COUPLES PREFER RESTURANTS WITH AN APPROXIMATE COST OF 300 RUPEES:
print(dataframe.head())

# Q5: WHICH MODE (ONLINE AND OFFLINE) HAS RECIEVED THE MAXIMUM RATING:

plt.figure(figsize=(6,6))
sns.boxplot(x="online_order",y="rate", data=dataframe)
plt.show()

#CONCLUSION: OFFLINE ORDER RECIEVED LOWER RATING IN COMPARSION TO ONLINE ORDER:
print(dataframe)
# Q6:WHICH TYPE OF RESTURANT RECIEVED MORE OFFLINE ORDERS, SO THAT ZOMATO CAN PAY CUSTOMERS  WITH SOME GOOD OFFER:
pivot_table=dataframe.pivot_table(index="listed_in(type)",columns="online_order",aggfunc='size',fill_value=0)
sns.heatmap(pivot_table,annot=True,cmap="YlGnBu",fmt="d")
plt.title("Heatmap",fontsize=20)
plt.xlabel("Online order",fontsize=15)
plt.ylabel("Listed in(type)",fontsize=15)
plt.show()

# CONCLUSION: DINING RESTURANT PRIMARILY ACCEPT OFFLINE ORDERS WHERE AS CAFE PRIMARILY RECIEVE ONLINE ORDERS. THIS SUGGEST THAT CLIENTS PREFER ORDERS IN PERSON AT RESTURANTS BUT PREFER ONLINE ORDERING ON CAFE:
