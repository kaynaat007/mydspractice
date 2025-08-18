import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


class LogisticRegression:

    def __init__(self, learning_rate, activation_function, features, output_labels, iterations):
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.X = features  # m * n
        self.Y = output_labels  # m by 1
        self.m, self.n = self.X.shape
        self.W = np.random.rand(self.n, 1)  # [n, 1] vector
        self.b = np.zeros((1, self.m))  # [1, m]  vector
        self.iterations = iterations

        assert self.m, 1 == output_labels.shape

    def get_activation_function(self):
        if self.activation_function == 'sigmoid':
            return lambda z: 1 / (1 + math.exp(-z))
        else:
            raise NotImplemented("activation function not implemented")

    def calculate_loss(self, y_hat, y):
        return -(y * math.log(y_hat) + (1 - y) * math.log(1 - y_hat))

    def display(self):
        print('learning rate: ', self.learning_rate)
        print('activation function: ', self.activation_function)
        print('# input examples: ', self.m)
        print("# features per example: ", self.n)
        print("shape of X: ", self.X.shape)
        print("shape of Y: ", self.Y.shape)

    def convert_feature_labels(self):
        le = LabelEncoder()
        n = len(self.X[0])
        for i in range(n):
            self.X[:, i] = le.fit_transform(self.X[:, i])
        return self.X

    def convert_output_label(self):
        label_mapping = {
            'unacc': 0,
            'acc': 1,
            'good': 2,
            'vgood': 3
        }
        self.Y['class'] = self.Y['class'].map(label_mapping)
        return self.Y

    def train(self):
        self.X = self.X.T

        for k in range(self.iterations):
            print('iteration #', k)
            # convert to [feature  *  examples] vector
            assert self.n, self.m == self.X.shape
            Z = np.dot(self.W.T, self.X) + self.b  # [1, n] * [n, m] + [1, m] == [1, m] vector
            activation_function = self.get_activation_function()
            for x, value in np.ndenumerate(Z):
                Z[x] = activation_function(value)
            A = Z
            assert (1, self.m) == Z.shape
            dz = A.T - self.Y  # [m, 1] - [m, 1] ==  [m, 1]
            dw = (np.dot(self.X, dz)) / self.m  # [n, m]  * [m, 1] == [n, 1]
            db = np.sum(dz) / self.m
            b_array = np.zeros((1, self.m), dtype=float)
            for x, value in np.ndenumerate(b_array):
                b_array[x] = self.learning_rate * db
            self.W = self.W - self.learning_rate * dw  # [n, 1]
            self.b = self.b - b_array  # [1, m]

    def predict(self, X_test, Y_test):
        '''
        :param X: given set of features [x1, x2, x3]
        :return: y_hat by trained values of W and B
        '''
        X_test = X_test.T
        assert (self.n, 1) == self.W.shape
        _, m = X_test.shape
        print("W.T shape: ", self.W.T.shape)
        print("X test shape: ", X_test.shape)
        b = self.b[0, 0:m].reshape((1, m))
        print("b shape: ", b.shape)
        Z = np.dot(self.W.T, X_test) + self.b   # [1, n] * [n, m] + [1, m] == [1, m] vector
        activation_function = self.get_activation_function()
        for x, value in np.ndenumerate(Z):
            Z[x] = activation_function(value)
        diff = Z - Y_test
        n = len(diff)
        non_zero_values = np.count_nonzero(diff)
        zero_values = n - non_zero_values
        accuracy = (zero_values / n) * 100.0
        return accuracy


def main():
    learing_rate = 0.01
    activation_function = 'sigmoid'
    iterations = 10
    data = pd.read_csv('/Users/bounce/practice/ml/data/car.data')
    features = data[[
        'buying',
        'maint',
        'safety'
    ]].values

    # label
    output_labels = data[['class']]
    X_train, X_test, Y_train, Y_test = train_test_split(features, output_labels, test_size=0.02)
    lr = LogisticRegression(learing_rate, activation_function, X_train, Y_train, iterations)
    lr.convert_feature_labels()
    lr.convert_output_label()
    lr.display()
    lr.train()
    x = X_test[0].reshape((lr.n, 1))
    print(x.shape)
    print(lr.predict(X_test, Y_test))

main()

