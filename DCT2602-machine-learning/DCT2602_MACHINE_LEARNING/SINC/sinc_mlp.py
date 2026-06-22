import sys

sys.path.append("../")

import matplotlib.pyplot as plt
import numpy as np

from DCT2602_MACHINE_LEARNING.utils.mlp import MLP


def sinc_example():
    X = np.linspace(-10, 10, 100).reshape(-1, 1)
    y = np.sinc(X).reshape(-1, 1)

    # Input: 1, Hidden: 10, 25, 100, 10, Output: 1
    # Activation function: Tanh(x) = 2 / (1 + exp(-2x)) - 1
    # Learning rate: 0.001, Epochs: 10000
    mlp = MLP(
        layer_sizes=[1, 10, 25, 100, 10, 1],
        learning_rate=0.001,
        epochs=10000,
        f="tanh",
        verbose=True,
    )

    mlp.train(X, y)

    predictions = mlp.predict(X)
    acc = [1 if np.abs(y[i] - predictions[i]) < 0.1 else 0 for i in range(len(y))]
    
    print("Sinc(x) Loss:", mlp.compute_loss(predictions, y))
    print("Sinc(x) Accuracy:", acc.count(1) / len(acc))

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(X, y, label="True sinc(x)", color="blue")
    plt.plot(X, predictions, label="MLP Approximation", color="red", linestyle="--")
    plt.title("Sinc(x) Function Approximation with MLP")
    plt.xlabel("x")
    plt.ylabel("sinc(x)")
    plt.legend()
    plt.show()


# Run examples
if __name__ == "__main__":
    sinc_example()
