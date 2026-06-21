from sklearn.neural_network import MLPRegressor
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 1, 0.01).reshape(-1, 1)
y = np.sinc(x).ravel()

nn = MLPRegressor(hidden_layer_sizes=(3), 
                  activation='tanh', solver='lbfgs')

n = nn.fit(x, y)

test_x = np.arange(-0.1, 1.1, 0.01).reshape(-1, 1)
test_y = nn.predict(test_x)

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, s=5, c='b', marker="o", label='real')
ax1.plot(test_x,test_y, c='r', label='NN Prediction')

plt.legend()
plt.show()