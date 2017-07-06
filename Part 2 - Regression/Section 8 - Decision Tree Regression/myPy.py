# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:30:27 2017

@author: Jaadugar
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv('Position_Salaries.csv')
X= dataset.iloc[:,1:2].values
y= dataset.iloc[:,2].values

from sklearn.tree import DecisionTreeRegressor
regressor= DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

y_pred= regressor.predict(6.5)

plt.scatter(X, y, color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title('Decision Tree')
plt.xlabel('Levels')
plt.ylabel('Salary')

X_grid=np.arange(min(X),max(X),0.01)
X_grid= X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.title('Decision Tree')
plt.xlabel('Levels')
plt.ylabel('Salary')
