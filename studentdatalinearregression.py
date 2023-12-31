# -*- coding: utf-8 -*-
"""StudentDataLinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12tyGUf0gWvmTSGsL908jqPIJVgcdTm2L

# **Importing Libraries To prepare the Data for some Co-Relation...**
# **Took Dataset from** : https://archive.ics.uci.edu/dataset/320/student+performance
"""

import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

"""# Reading CSV (Full Form : Comma Seprated Value...)"""

data = pd.read_csv('/content/student-mat.csv', sep=';')

data.head()

data = data[["G1","G2","G3","studytime","failures","absences"]]
print(data.head()) # so here we can notice all data is Int not any other type..

"""# So what we want from this Data, we want the Final Grade Should be good."""

predict = "G3"
X = np.array(data.drop([predict], 1)) # This is our train thing..
Y = np.array(data[predict])           # This is our Prediction / output Feature..

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X , Y , test_size = 0.1)

linear = linear_model.LinearRegression()
linear.fit(x_train , y_train)
accuracy = linear.score(x_test , y_test)
print(accuracy)

print('Coff : \n ', + linear.coef_) # all Five coeff we are getting here as we selected in our Data-Set
print('Intercept : \n ', + linear.intercept_) # And here are getting our Intercept...

predictions = linear.predict(x_test) # here we are telling Model to predict the output should be..

for x in range(len(predictions)):
  output = (int(predictions[x]), x_test[x], y_test[x])
  print("Actual-Output : Array of Data : Machine-OutPut")
  print(output) # Model Output = [ G1, G2 , G3, studytime, Failure, Absence]