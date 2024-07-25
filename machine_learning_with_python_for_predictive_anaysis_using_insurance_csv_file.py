# -*- coding: utf-8 -*-
"""Machine Learning with python for predictive anaysis using Insurance_csv file

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g-vR6KB2mK9HyvDkRq0uQ5hPHKOiaW1I
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('insurance.csv')

data.head()

df.shape

print("The first row count of the data set{}",format(data.shape[0]))

data.info()

data.isna().sum()

data.describe()

data.duplicated().sum()

data.drop_duplicates(inplace=True)

data.duplicated().sum()

data.value_counts()

data.value_counts("sex")

sns.countplot(x="sex",data=data, color = "r")
plt.show()

data.value_counts("smoker")

sns.countplot(x="smoker",data=data)
plt.show()

data.value_counts("region")

sns.countplot(x="region",data = data)
plt.show()

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing

Labelencoder = LabelEncoder()

data.head()

data["sex"] = Labelencoder.fit_transform(data["sex"])
data["smoker"] = Labelencoder.fit_transform(data["smoker"])
data["region"] = Labelencoder.fit_transform(data["region"])

data.head()

data.corr()

data.corr()["charges"].sort_values(ascending=False)

sns.heatmap(data.corr(),annot=True)
plt.show()

sns.heatmap(data.corr(),annot=True, cmap="rainbow");

for i in data.columns:
  sns.displot(x=data[i])
  plt.title(i + " " + "distribution")
  plt.show()

colorsforx = ["red","green","yellow","black", "blue", "grey"]
colorschanger = 0

for i in data.columns[:-1]:
  sns.scatterplot(data=data, x=i, y="charges", color=colorsforx[colorschanger])


  plt.show()

  colorschanger += 1

x = data[["age", "sex", "bmi", "children","smoker", "region"]]
y = data["charges"]

from sklearn.model_selection import train_test_split

x_train,x_test, y_train, y_test = train_test_split(x,y, test_size=0.30)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_x_train = scaler.fit_transform(x_train)
scaled_x_test = scaler.transform(x_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error

def modelresults(predictions):
  print("Mean absolute error on model is {}".format(mean_absolute_error(y_test,predictions)))
  print("Mean squared error on model is {}".format(np.sqrt(mean_squared_error(y_test,predictions))))

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(scaled_x_train, y_train)

predslr = lr.predict(scaled_x_test)
modelresults(predslr)

from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV

svrmodel = SVR()
param_gridsvr = {"C":[0.001, 0.01, 0.1, 0.5, 1.0],
                 "kernel": ["linear", "rbf", "poly"],
                 "gamma":["scale", "auto"],
                 "degree":[2,3,4,5]}
gridsvr = GridSearchCV(svrmodel, param_gridsvr)
gridsvr.fit(scaled_x_train, y_train)
print("Best parameters for model is {}".format(gridsvr.best_params_))

predsgridsvr= gridsvr.predict(scaled_x_test)
modelresults(predsgridsvr)

from  sklearn.ensemble import RandomForestRegressor
rfrmodel = RandomForestRegressor()
param_gridrfr= {"bootstrap": [True],
                 "max_depth": [5,10,15],
                 "max_features": ["auto", "log2"],
                 "n_estimators" : [2,3,4,5,6,7,8,9,10]}
gridrfr= GridSearchCV(rfrmodel, param_gridrfr)
gridrfr.fit(scaled_x_train, y_train)

predsgridrfr = gridrfr.predict(scaled_x_test)
modelresults(predsgridrfr)

x.columns

columniterate = 1
for index in x.columns:
  mean = data[index].mean()
  print("The mean of the column {} is {}".format(columniterate, mean))

new_customer = np.array([39, 0, 30, 1, 0, 1])

gridrfr.predict(new_customer.reshape(1,-1))

print("The Insurance cost of new customer is {}".format(gridrfr.predict(new_customer.reshape(1,-1))[0]))