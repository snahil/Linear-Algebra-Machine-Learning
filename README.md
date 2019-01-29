# Linear-Algebra-Machine-Learning


> Dependency
	
	"import pandas library"

In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. It is free software released under the three-clause BSD license.

	"import sklearn"

	Scikit-learn is a free software machine learning library for the Python programming language. It features various classification, regression and clustering algorithms including support vector machines,




> Resolving Dependency 

 > Using pip command line # for python version 2
  	i.e pip install pandas
 > Using pip  command line # for python version 3
 	i.e pip3 install pandas
 > we are using only specfic features of the "sklearn"
	i.e from sklearn.preeprocessing import lableEncoder
 	



pandas.DataFrame.iloc

DataFrame.iloc

    Purely integer-location based indexing for selection by position.

    .iloc[] is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.

    Allowed inputs are:

        An integer, e.g. 5.
        A list or array of integers, e.g. [4, 3, 0].
        A slice object with ints, e.g. 1:7.
        A boolean array.
        A callable function with one argument (the calling Series, DataFrame or Panel) and that returns valid output for indexing (one of the above). This is useful in method chains, when you don’t have a reference to the calling object, but would like to base your selection on some value.

    .iloc will raise IndexError if a requested indexer is out-of-bounds, except slice indexers which allow out-of-bounds indexing (this conforms with python/numpy slice semantics).
    
For more details refer to - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html(Text Refrence)
