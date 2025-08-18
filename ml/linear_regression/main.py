'''

how Linear regression works ?
----------------



'''

import numpy as np
import pandas as pd
from sklearn import neighbors, metrics
from sklearn import datasets, linear_model, model_selection
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from matplotlib import pyplot as plt


'''

playing with numpy.ndarray 
-----------------------------
print(type(X[:, 0]))
print(X.shape)
print(X.dtype)
# print(X[0,0], X[0,1], X[0,2])
# print(X[1, 0], X[1, 1], X[1, 2])
print(X[:, 0])
print(X[:, 1])
print(X[:, 2])
# y = X[:, 0]
# print(y[0], y[1], y[2])

'''


data = pd.read_csv('/Users/bounce/practice/ml/data/car.data')
# take a look at data
print(data.head())


def convert_feature_labels(X):
    le = LabelEncoder()
    n = len(X[0])
    for i in range(n):
        X[:, i] = le.fit_transform(X[:, i])
    return X


def convert_output_label(output_labels):
    label_mapping = {
        'unacc': 0,
        'acc': 1,
        'good': 2,
        'vgood': 3
    }
    # print(type(output_labels))
    # print(type(output_labels['class']))
    output_labels['class'] = output_labels['class'].map(label_mapping)
    print(type(output_labels))
    return output_labels
    # print(output_labels)


def call_main():

    boston = datasets.load_boston() # sklearn.utils._bunch.Bunch'
    features = boston.data  # ndarray (506,13)
    output_labels = boston.target  # ndarray  (506,)

    print("boston")
    print(type(boston))
    print("features")
    print(features)
    print(features.shape)
    print(type(features))
    print("output labels")
    print(output_labels)
    print(type(output_labels))
    print(output_labels.shape)

    linear_regression(features, output_labels)


def linear_regression(features, output_labels):
    # algorithm
    l_reg = linear_model.LinearRegression()

    #plt.scatter(features.T[5], output_labels)
    #plt.show()
    X_train, X_test, y_train, y_test  = train_test_split(features, output_labels, test_size=0.02)

    # train
    model = l_reg.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("predictions: ", predictions)
    print("r square value: ", l_reg.score(features, output_labels))
    print("coedd:", l_reg.coef_)
    print("intercept: ", l_reg.intercept_)





call_main()

