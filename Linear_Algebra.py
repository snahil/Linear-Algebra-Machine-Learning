import pandas as pd # we are giving name of panda library as pd
from sklearn.linear_model import LinearRegression #we are importing  a specfic package form the library for opt the code
package from the 
import matplotlib.pyplot as plt  # library for ploting graph

dataset=pd.read_csv('marks.csv')


y =  dataset.iloc[:,-1]   # The iolic indexer for pandas is used for integer based location

X = dataset.iloc[:, 0:1] # x will be always in captial ": means print all the row or coloum which ever comes first" 
# press x or y for printing the data set

model = LinearRegression()

model.fit(X,y)


model.fit

model.predict([[7]])



plt.scatter(X, y) # ploating Graph in 1 DeprecationWarning


plt.plot(X,y) # Graph ploating in 2D 
