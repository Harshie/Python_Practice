# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:46:20 2020

@author: ehars
"""


# Importing pandas for grocery dataset
import pandas as pd

# Importing grocery data
sales_data2 = pd.read_csv("grocery_sales.csv") 

# Filling the missing value
sales_data1 = sales_data

# Dropping null rows
sales_data1 = sales_data1[sales_data1["sales"].notnull()]

#Filling null rows
avg_sales = sales_data["sales"].mean()
sales_data['sales'].fillna(value = avg_sales,inplace = True)

#printing selected rows
sales_data.loc[sales_data["transaction_date"] == '2020-09-01']

# Summary
Summary = sales_data.groupby("transaction_date")["sales"].sum()

#plotting
Summary.plot()
Summary.plot(rot=45)
