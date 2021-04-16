# Zaú Júlio A. Galvão

import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Serialized vowels in a one-dimensional array
_vowels = {
    'a': [
        1, 1, 1,
        1, 0, 1,
        1, 1, 1,
        1, 0, 1,
        1, 0, 1],
    'e': [
        1, 1, 1,
        1, 0, 0,
        1, 1, 1,
        1, 0, 0,
        1, 1, 1],
    'i': [
        0, 1, 0,
        0, 1, 0,
        0, 1, 0,
        0, 1, 0,
        0, 1, 0],
    'o': [
        1, 1, 1,
        1, 0, 1,
        1, 0, 1,
        1, 0, 1,
        1, 1, 1],
    'u': [
        1, 0, 1,
        1, 0, 1,
        1, 0, 1,
        1, 0, 1,
        1, 1, 1]
}
##################################################
# Separation of the vowel dictionary keys
keys = [*_vowels]

# Arrangement labels with 1000 vowels
y = np.array([keys[label] for label in range(0, 5) for i in range(1000)])

# Arrangement of samples based on labels => (y)
X = np.array([_vowels[i] for i in y])

# Separation of training set and test |30% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)
##################################################

##################################################
# Tol = Stop criterion
# ETA0 = Learning fee
# MAX_ITER = iterations limit
clf = Perceptron(tol=1e-3, eta0=0.1, max_iter=20)  # ,Verbose=1)

# Training using stochastic gradient descent with training set
clf.fit(X_train, y_train)
##################################################

##################################################
# Applying Perceptron Trained in X Data to Estimate Set Y
y_pred = clf.predict(X_test)

print("Validation set: ", y_test)
print("Estimated set: ", y_pred)

# Average accuracy
print('Accuracy: %.2f %%' % (accuracy_score(y_test, y_pred)*100))

print("\nSimple Test =>")

print("Labels : ", 'a, i, e, u, o')
print("Predict: ",
      clf.predict(
          [_vowels['a'],
           _vowels['i'],
           _vowels['e'],
           _vowels['u'],
           _vowels['o']]
      ))

err1 = [[
    1, 1, 1,
    1, 1, 1,
    1, 1, 1,
    1, 1, 1,
    1, 1, 1
]]

print("Error attempt - all 1: ", err1)
print("Classification      :", clf.predict(err1))
##################################################

print("\Synaptic weights: \n", clf.coef_)
print(f"""
Network architecture: {clf.coef_.shape},
{clf.coef_.shape[0]} Neurons
{clf.coef_.shape[1]} Weights every,
Single layer
""")
