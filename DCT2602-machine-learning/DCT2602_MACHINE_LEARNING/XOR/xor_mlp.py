import sys

sys.path.append("../")

import matplotlib.pyplot as plt
import numpy as np

from DCT2602_MACHINE_LEARNING.utils.mlp import MLP


def plot_decision_boundary(X, y, mlp, title="Decision Boundary: XOR + MLP"):
    """
    Plot the decision boundary of the MLP on the XOR problem.

    Args:
        X (np.ndarray): Input features.
        y (np.ndarray): Target values.
        mlp (MLP): Trained MLP model.
        title (str): Title of the plot.
    """
    # Define the bounds of the plot
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

    # Create a mesh grid
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = mlp.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = (Z > 0.5).astype(int)  # Binary classification

    # Reshape the output to fit the mesh grid
    Z = Z.reshape(xx.shape)

    # Plot the decision boundary
    cmap = plt.cm.get_cmap("RdYlBu")

    plt.contourf(xx, yy, Z, alpha=0.8, cmap=cmap)
    plt.scatter(X[:, 0], X[:, 1], c=y.flatten(), edgecolors="k", cmap=cmap)
    plt.title(title)
    plt.show()


def xor_example():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    mlp = MLP(layer_sizes=[2, 4, 1], learning_rate=0.1, epochs=10000, verbose=True)
    mlp.train(X, y)

    predictions = mlp.predict(X)
    # Binary classification
    predicted_classes = (predictions > 0.5).astype(int)

    print("XOR Problem Predictions:")
    print(predicted_classes.flatten())

    # Calculate accuracy
    accuracy = np.mean(predicted_classes == y) * 100
    print(f"Accuracy: {accuracy:.2f}%")

    # Plot decision boundary
    plot_decision_boundary(X, y, mlp)


if __name__ == "__main__":
    xor_example()
