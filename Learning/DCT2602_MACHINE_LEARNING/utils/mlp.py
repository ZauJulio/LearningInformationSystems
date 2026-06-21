import numpy as np

from DCT2602_MACHINE_LEARNING.utils.activation_functions import (
    reLu,
    reLu_derivative,
    sigmoid,
    sigmoid_derivative,
    softmax,
    softmax_derivative,
    tanh,
    tanh_derivative,
)


class MLP:
    """
    A simple Multi-Layer Perceptron (MLP) neural network class with backpropagation.

    Args:
        layer_sizes (list of int): List containing the number of neurons in each layer.
        learning_rate (float): Learning rate for weight updates.
        epochs (int): Number of training epochs.
        f (str): Activation function to use. Can be 'sigmoid' or 'reLu'.
        verbose (bool): Whether to print detailed training information.
    """

    def __init__(
        self,
        layer_sizes: list[int],
        learning_rate: float = 0.01,
        epochs: int = 1000,
        f: str = "sigmoid",
        verbose: bool = False,
    ):
        self.layer_sizes = layer_sizes
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.verbose = verbose

        if f == "sigmoid":
            self.activation = sigmoid
            self.activation_derivative = sigmoid_derivative
        elif f == "reLu":
            self.activation = reLu
            self.activation_derivative = reLu_derivative
        elif f == "tanh":
            self.activation = tanh
            self.activation_derivative = tanh_derivative
        elif f == "softmax":
            self.activation = softmax
            self.activation_derivative = softmax_derivative
        else:
            raise ValueError("Activation function must be 'sigmoid' or 'reLu'.")

        self.initialize_weights()

    def initialize_weights(self) -> None:
        """
        Initialize weights and biases for the MLP.

        Args:
            None

        Returns:
            None
        """
        self.weights = []
        self.biases = []

        for i in range(len(self.layer_sizes) - 1):
            lw = np.random.randn(self.layer_sizes[i], self.layer_sizes[i + 1])
            lb = np.zeros((1, self.layer_sizes[i + 1]))

            self.weights.append(lw)
            self.biases.append(lb)

    def forward(self, X: np.ndarray) -> np.ndarray:
        """
        Perform forward propagation to compute the output of the network.

        Args:
            X (np.ndarray): Input data of shape (n_samples, n_features).

        Returns:
            np.ndarray: Output of the MLP after forward propagation.
        """
        # Initialize activations list with the input data.
        self.a = [X]
        # Initialize acc of linear combinations (z) for each layer.
        self.z = []

        # Iterate over each layer's weights and biases.
        for W, b in zip(self.weights, self.biases):
            # Compute the linear combination (z = a_prev * W + b).
            z = np.dot(self.a[-1], W) + b
            a = self.activation(z)

            self.z.append(z)
            self.a.append(a)

        # Return the final activation, which is the output of the MLP.
        return self.a[-1]

    def backward(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Perform backpropagation to compute the gradient and update weights.

        Args:
            X (np.ndarray): Input data of shape (n_samples, n_features).
            y (np.ndarray): True labels of shape (n_samples, n_output).

        Returns:
            None
        """
        # Number of samples in the batch.
        m = y.shape[0]
        # Compute the gradient of the loss with respect to the output (dL/da).
        d_a = np.subtract(self.a[-1], y)
        # Compute the gradient of the loss with respect to the linear combination (z)
        # at the output layer (dL/dz).
        d_z = d_a * self.activation_derivative(self.a[-1])

        d_weights = []
        d_biases = []

        # Iterate backward through the layers to compute gradients.
        for i in reversed(range(len(self.weights))):
            # Compute the gradient of the loss with respect to the weights (dL/dW).
            d_w = np.dot(self.a[i].T, d_z) / m
            # Compute the gradient of the loss with respect to the biases (dL/db).
            d_b = np.sum(d_z, axis=0, keepdims=True) / m

            d_weights.append(d_w)
            d_biases.append(d_b)

            # Compute the gradient of the loss with respect to the activations of the
            # previous layer, if not at the input layer.
            if i > 0:
                d_a = np.dot(d_z, self.weights[i].T)
                # Compute the gradient of the loss with respect to the linear combination
                # (z) of the previous layer.
                d_z = d_a * self.activation_derivative(self.a[i])

        # Reverse the gradients lists to align with the forward pass.
        d_weights.reverse()
        d_biases.reverse()

        # Update the weights and biases using the computed gradients.
        for i in range(len(self.weights)):
            self.weights[i] -= self.learning_rate * d_weights[i]
            self.biases[i] -= self.learning_rate * d_biases[i]

    def compute_loss(self, y_pred: np.ndarray, y_true: np.ndarray):
        """
        Compute the mean squared error loss.

        Args:
            y_pred (np.ndarray): Predicted output.
            y_true (np.ndarray): True output.

        Returns:
            float: Mean squared error loss.
        """
        return np.mean((y_pred - y_true) ** 2)

    def compute_accuracy(self, y_pred: np.ndarray, y_true: np.ndarray) -> float:
        """
        Compute the accuracy of predictions.

        Args:
            y_pred (np.ndarray): Predicted output (probabilities).
            y_true (np.ndarray): True output.

        Returns:
            float: Accuracy as a percentage.
        """
        y_pred_class = (y_pred > 0.5).astype(int)  # Assuming binary classification
        return np.mean(y_pred_class == y_true) * 100

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Train the MLP using the provided data.

        Args:
            X (np.ndarray): Input data.
            y (np.ndarray): Target data.

        Returns:
            None
        """
        for epoch in range(self.epochs):
            y_pred = self.forward(X)
            self.backward(X, y)

            # Compute loss and accuracy for verbose mode
            if self.verbose and (epoch % 100 == 0 or epoch == self.epochs - 1):
                loss = self.compute_loss(y_pred, y)
                accuracy = self.compute_accuracy(y_pred, y)
                print(
                    f"Epoch {epoch + 1}/{self.epochs}, Loss: {loss:.4f}, Accuracy: {accuracy:.2f}%"
                )

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions using the trained MLP.

        Args:
            X (np.ndarray): Input data.

        Returns:
            np.ndarray: Predicted output.
        """
        return self.forward(X)
