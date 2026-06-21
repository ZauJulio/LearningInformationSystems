import numpy as np


def tanh(x: np.ndarray) -> np.ndarray:
    """
    Compute the tanh function.

    Args:
        x (np.ndarray): Input data.

    Returns:
        np.ndarray: Output of the tanh function.
    """
    return np.tanh(x)


def tanh_derivative(x: np.ndarray) -> np.ndarray:
    """
    Compute the derivative of the tanh function.

    Args:
        x (np.ndarray): Input data.

    Returns:
        np.ndarray: Derivative of the tanh function.
    """
    return 1 - np.tanh(x) ** 2


def softmax(x: np.ndarray) -> np.ndarray:
    """
    Compute the softmax function.

    Args:
        x (np.ndarray): Input data.

    Returns:
        np.ndarray: Output of the softmax function.
    """
    exps = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exps / np.sum(exps, axis=-1, keepdims=True)


def softmax_derivative(x: np.ndarray) -> np.ndarray:
    """
    Compute the derivative of the softmax function.

    Args:
        x (np.ndarray): Input data.

    Returns:
        np.ndarray: Derivative of the softmax function.
    """
    return x * (1 - x)


def reLu(x: np.ndarray) -> np.ndarray:
    """
    Compute the ReLU function.

    Args:
        x (np.ndarray): Input data.

    Returns:
        np.ndarray: Output of the ReLU function.
    """
    return np.maximum(0, x)


def reLu_derivative(x: np.ndarray) -> np.ndarray:
    """
    Compute the derivative of the ReLU function.

    Args:
        x (np.ndarray): Input data.

    Returns:
        np.ndarray: Derivative of the ReLU function.
    """
    return 1.0 * (x > 0)


def sigmoid(x: np.ndarray) -> np.ndarray:
    """
    Compute the sigmoid function.

    Args:
        x (np.ndarray): Input data.

    Returns:
        np.ndarray: Output of the sigmoid function.
    """
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x: np.ndarray) -> np.ndarray:
    """
    Compute the derivative of the sigmoid function.

    Args:
        x (np.ndarray): Input data.

    Returns:
        np.ndarray: Derivative of the sigmoid function
    """
    return x * (1 - x)
