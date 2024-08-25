import sys

sys.path.append("../")

from matplotlib import legend
import matplotlib.pyplot as plt
import numpy as np

from DCT2602_MACHINE_LEARNING.utils.rbf import RBFNetwork


def plot_decision_boundary(
    X: np.ndarray, y: np.ndarray, rbf: RBFNetwork, title: str = "Decision Boundary: XOR + RBF"
) -> None:
    """
    Plot the decision boundary of the rbf on the XOR problem.

    Args:
        X (np.ndarray): Input features.
        y (np.ndarray): Target values.
        rbf (RBFNetwork): Trained rbf model.
        title (str): Title of the plot.
    """
    # Define the bounds of the plot
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

    # Create a mesh grid
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = rbf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = (Z > 0.5).astype(int)  # Binary classification

    # Reshape the output to fit the mesh grid
    Z = Z.reshape(xx.shape)

    # Plot the decision boundary
    cmap = plt.cm.get_cmap("RdYlBu")

    plt.contourf(xx, yy, Z, alpha=0.8, cmap=cmap)
    plt.scatter(X[:, 0], X[:, 1], c=y.flatten(), edgecolors="k", cmap=cmap, label="True XOR")
    plt.title(title)
    plt.show()


def xor_example():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])

    # Initialize and train the RBF network
    rbf_network = RBFNetwork(centers=np.array([[0, 1], [1, 0]]), sigma=0.5)
    rbf_network.fit(X, y)

    # Predict the XOR problem
    predictions = rbf_network.predict(X)
    predicted_classes = (predictions > 0.5).astype(int)

    print("XOR Problem Predictions:")
    print(predicted_classes.flatten())

    # Calculate accuracy
    accuracy = np.mean(predicted_classes == y) * 100
    print(f"Accuracy: {accuracy:.2f}%")

    plot_decision_boundary(X, y, rbf_network)


if __name__ == "__main__":
    xor_example()
