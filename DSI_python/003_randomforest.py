# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:44:22 2020

@author: ehars
"""


from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd

#Importing the dataset

gamedataset = pd.read_csv("video_game_data.csv")

#Splitting the covariates

X = gamedataset.drop(["completion_time"],axis = 1)
y = gamedataset["completion_time"]

# Splitting the data for training and testing

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size =0.2, random_state = 42)

#Initiate the model object

regressor = RandomForestRegressor(random_state=42)

# Fitting or training the model

regressor.fit(X_train, y_train)

# Assess model accuracy

y_pred = regressor.predict(X_test)

pred_comparison = pd.DataFrame({"actual" : y_test,
                                "predicted" : y_pred})

r2_score(y_test,y_pred)
# The r2 score is 0.6657934159750488 which is good for the model. The prediction values when compared with each other in the pred_comparison field, shows the similar results.