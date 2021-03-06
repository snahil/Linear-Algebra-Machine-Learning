import pandas as pd # Using numpy as np for easy call in the program 
import matplotlib.pyplot as plt
import sklearn


dataset = pd.read_csv('Salary_Data.csv') # keep the CSV file in the same folder

y = dataset.iloc[:,-1]

y.shape # To check the dim of y (2 D or oneD) as the system will not accept one D variable 


X = dataset.iloc[:, 0:1]

X.shape # same as above


plt.scatter(X,y) # TO plote a Graph


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=42)


X_train.shape  # For Training the dataset


y_train.shape # Same as Above


model = LinearRegression()  # Devloping the LR model by importing it from sklearn


model.fit(X_train, y_train)

y_pred = model.predict(X_test) # For Predecting the data y_tain Dataset

y_pred # to check the predected output
