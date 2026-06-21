import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC
from data import vowels, keys

# Arrangement labels with 1000 vowels
y = np.array([keys[label] for label in range(0, 5) for i in range(1000)])

# Arrangement of samples based on labels => (y)
X = np.array([vowels[i] for i in y])

# Separation of training set and test |30% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)
##################################################

# Gamma coefficient is auto == (1 / n_features)
# Fit classifiers
clfs = {
    'rbf': SVC(kernel='rbf', gamma='auto').fit(X_train, y_train),
    'poly': SVC(kernel='poly', degree=5, gamma='auto').fit(X_train, y_train),
    'sigmoid': SVC(kernel='sigmoid', gamma='auto').fit(X_train, y_train),
    'linear': SVC(kernel='linear').fit(X_train, y_train)
}

print("""Error Test attempt - all 1:
    1 1 1
    1 1 1
    1 1 1
    1 1 1
    1 1 1
""")

for kernel, clf in zip(clfs.keys(), clfs.values()):
    ##################################################
    # Applying Perceptron Trained in X Data to Estimate Set Y
    score = accuracy_score(y_test, clf.predict(X_test))

    # Average accuracy
    print('Accuracy %s: %.2f %%' % (kernel, (score*100)))

    err1 = [[
        1, 1, 1,
        1, 1, 1,
        1, 1, 1,
        1, 1, 1,
        1, 1, 1
    ]]

    print("Classification Error Test - All 1: [%s] \n" % clf.predict(err1)[0])
