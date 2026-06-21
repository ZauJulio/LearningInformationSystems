from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

import matplotlib.pyplot as plt
import numpy as np


def polyReg(X_train, y_train, X_test):
    poly = PolynomialFeatures(degree=5)

    reg = linear_model.LinearRegression().fit(
        poly.fit_transform(X_train),
        y_train
    )
    
    return reg.predict(poly.fit_transform(X_test))

# Set Data and Train
X_train = np.arange(0.0, 10, 0.01).reshape(-1, 1)
y_train = np.sinc(X_train).ravel() # sin(pi * x)/(pi * x)

model = MLPRegressor(
    hidden_layer_sizes=(10,10),
    activation='tanh',
    solver='lbfgs',
    max_iter=10000
)

model.fit(X_train, y_train)

# Test
X_test = np.arange(-0.1, 11, 0.01).reshape(-1, 1)
y_test = np.sinc(X_test).ravel()
y_pred = model.predict(X_test)

error = np.sqrt(mean_squared_error(y_test, y_pred))

polyRegression = polyReg(X_train, y_train, X_test)

print('Accuracy: %.8f' % model.score(X_test, y_pred))
print('RMSE: %.8f' % error)

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(X_train, y_train, s=5, c='b', marker="o", label='Train')
ax1.plot(X_test, y_pred, c='r', label='Prediction')
ax1.plot(X_test, polyRegression, c='g', label='Linear Regression 5º')

plt.legend()
plt.show()
