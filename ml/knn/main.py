'''

how KNN works ?
----------------



'''




import numpy as np
import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


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
    # we are taking only three features
    features = data[[
        'buying',
        'maint',
        'safety'
    ]].values

    # label
    output_labels = data[['class']]

    # conversion
    features = convert_feature_labels(features)
    output_labels = convert_output_label(output_labels)
    knn(features, output_labels)

'''
KNN - N nearest neighbour 
'''
def knn(features, output_labels):

    knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights='uniform')
    X_train, X_test, Y_train, Y_test = train_test_split(features, output_labels, test_size=0.02)

    knn.fit(features, output_labels)
    predictions = knn.predict(X_test)
    print(X_train.shape)
    print(X_test.shape)
    print(Y_train.shape)
    print(Y_test.shape)
    print(predictions.shape)
    # compare output from the model == output from our test sample
    accuracy = metrics.accuracy_score(Y_test, predictions)
    # print('predictions: ', predictions)
    print('accuracy: ', accuracy)

    a = 20
    print("output shape: ", output_labels.shape)
    print("output type: ", type(output_labels))
    print("actual value: ",  output_labels[a])
    # print("predicted value: ", knn.predict(features)[a])



call_main()

