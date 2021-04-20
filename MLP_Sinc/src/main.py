from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

import numpy as np

# Set Data and Train
X_train = np.arange(0.0, 10, 0.01).reshape(-1, 1)
y_train = np.sinc(X_train).ravel()

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
print('Accuracy: %.8f' % model.score(X_test, y_pred))
print('RMSE: %.8f' % error)