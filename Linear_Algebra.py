import pandas as pd # we are giving name of panda library as pd
form sklearn.linearmodelform sklearn.linearmodel #we are importing  a specfic package form the library for opt the code
package from the 

dataset=pd.read_csv('marks.csv')

y =  dataset.iloc[:,-1]   # The iolic indexer for pandas is used for integer based location
x = dataset.iloc[:,0:1]

model = LinearRegression()


model.fit
