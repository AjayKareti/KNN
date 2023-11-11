#import necessary Libraries 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris
from sklearn import preprocessing
from sklearn import neighbors
import matplotlib.pyplot as plt


#loading datasets
iris=load_iris()
X=iris.data
y=iris.target
#split the data into training and test data 
X_train,X_test,y_train,y_test=train_test_split(X,y,stratify=y,random_state=0,train_size=0.7)

# display data
X

# displaying the target values
y

#preprocessing the dataset
scaler=preprocessing.StandardScaler().fit(X_train)
X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)

# train the data using fit() function and predict the test set
knn=neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_testt)

#displaying accuracy of the model
print(accuracy_score(y_test,y_pred))

# dispalying performance of the model
print("Training set score:{:.3f}".format(knn.score(X_train,y_train)))
print("Test set score:{:.3f}".format(knn.score(X_test,y_test)))





