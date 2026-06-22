import numpy as np
from typing import Callable


class RBFNetwork:
    """
    Radial Basis Function (RBF) Neural Network for solving binary classification problems such as XOR.

    args:
        centers (np.ndarray): The centers (centroids) for the RBF neurons.
        sigma (float): The spread (standard deviation) of the Gaussian functions.
        weights (np.ndarray): The weights of the output layer.
        rbf_function (Callable[[np.ndarray, np.ndarray, float], float]): The RBF function, typically a Gaussian.
    """

    def __init__(
        self,
        centers: np.ndarray,
        sigma: float,
        weights: np.ndarray = np.array([]),
        rbf_function: Callable[[np.ndarray, np.ndarray, float], float] | None = None,
    ):
        """
        Initialize the RBF network with specified centers and sigma.

        Args:
            centers (np.ndarray): The centers (centroids) for the RBF neurons.
            sigma (float): The spread (standard deviation) of the Gaussian functions.
        """
        self.centers = centers
        self.sigma = sigma
        self.weights = weights
        self.rbf_function = rbf_function or self.gauss_rbf

    def gauss_rbf(self, x: np.ndarray, center: np.ndarray, sigma: float) -> float:
        """
        Gaussian Radial Basis Function (RBF).

        Args:
            x (np.ndarray): Input vector.
            center (np.ndarray): Center vector.
            sigma (float): Spread of the Gaussian function.

        Returns:
            float: The computed RBF value.
        """
        # Formula: exp(-||x - center||^2 / (2 * sigma^2))
        return np.exp(-(np.linalg.norm(x - center) ** 2) / (2 * sigma**2))

    def _construct_design_matrix(self, X: np.ndarray) -> np.ndarray:
        """
        Construct the design matrix using the RBF function.

        Args:
            X (np.ndarray): Input data.

        Returns:
            np.ndarray: The design matrix.
        """
        # Initialize the design matrix
        G = np.zeros((X.shape[0], len(self.centers)))

        for i, x in enumerate(X):
            # Compute the RBF values for each center
            for j, center in enumerate(self.centers):
                G[i, j] = self.rbf_function(x, center, self.sigma)

        return G

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Train the RBF network using the provided training data.

        Args:
            X (np.ndarray): Training input data.
            y (np.ndarray): Training output data.
        """
        # Construct the design matrix
        G = self._construct_design_matrix(X)

        # Solve for the weights using least-squares solution
        self.weights, _, _, _ = np.linalg.lstsq(G, y)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict the output for the given input data.

        Args:
            X (np.ndarray): Input data to predict.

        Returns:
            np.ndarray: Predicted output data.
        """
        G = self._construct_design_matrix(X)

        return G.dot(self.weights)

    def compute_loss(self, y_pred: np.ndarray, y_true: np.ndarray):
        """
        Compute the mean squared error loss between the predicted and true values.

        Args:
            y_pred (np.ndarray): Predicted values.
            y_true (np.ndarray): True values.

        Returns:
            float: The computed loss value.
        """
        return np.mean((y_pred - y_true) ** 2)

    def compute_accuracy(self, y_pred: np.ndarray, y_true: np.ndarray) -> float:
        """
        Compute the accuracy of the predicted values.

        Args:
            y_pred (np.ndarray): Predicted values.
            y_true (np.ndarray): True values.

        Returns:
            float: The computed accuracy value.
        """
        return np.mean(y_pred == y_true)
