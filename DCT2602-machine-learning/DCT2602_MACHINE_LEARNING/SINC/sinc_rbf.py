import sys

sys.path.append("../")

import matplotlib.pyplot as plt
import numpy as np

from DCT2602_MACHINE_LEARNING.utils.rbf import RBFNetwork


def sinc_example():
    X = np.linspace(-10, 10, 100).reshape(-1, 1)
    y = np.sinc(X)

    rbf = RBFNetwork(centers=np.linspace(-10, 10, 15), sigma=1.0)
    rbf.fit(X, y)

    predictions = rbf.predict(X)
    acc = [1 if np.abs(y[i] - predictions[i]) < 0.1 else 0 for i in range(len(y))]

    print("Sinc(x) Loss:", rbf.compute_loss(predictions, y))
    print("Accuracy:", np.mean(acc))

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(X, y, label="True sinc(x)", color="blue")
    plt.plot(X, predictions, label="RBF Approximation", color="red", linestyle="--")
    plt.title("Sinc(x) Function Approximation with RBF")
    plt.xlabel("x")
    plt.ylabel("sinc(x)")
    plt.legend()
    plt.show()


# Run examples
if __name__ == "__main__":
    sinc_example()
