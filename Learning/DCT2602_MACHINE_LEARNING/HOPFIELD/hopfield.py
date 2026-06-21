import numpy as np
from typing import List
from itertools import product


class HopfieldNetwork:
    def __init__(self, size: int):
        """
        Initialize the Hopfield network with a specified number of neurons.

        Args:
            size (int): The number of neurons in the network.
        """
        self.size: int = size
        self.weights: np.ndarray = np.zeros((size, size))

    def train(self, patterns: List[np.ndarray]) -> None:
        """
        Train the Hopfield network using the Hebbian learning rule.

        Args:
            patterns (List[np.ndarray]): List of binary patterns to be stored in the network.
        """
        num_patterns: int = len(patterns)

        for pattern in patterns:
            pattern = pattern.reshape(self.size, 1)
            self.weights += pattern @ pattern.T  # Outer product

        self.weights /= num_patterns  # Normalize weights by the number of patterns

        # Ensure no neuron has self-connection
        np.fill_diagonal(self.weights, 0)

    def update(self, pattern: np.ndarray, synchronous: bool = False) -> np.ndarray:
        """
        Update the network state based on the input pattern.

        Args:
            pattern (np.ndarray): The input pattern to be updated.
            synchronous (bool): Whether to update neurons synchronously or asynchronously.

        Returns:
            np.ndarray: The updated pattern.
        """
        if synchronous:
            return np.sign(self.weights @ pattern)
        else:
            for i in range(self.size):
                raw_value: float = np.dot(self.weights[i], pattern)
                pattern[i] = 1 if raw_value >= 0 else -1

        return pattern

    def recall(
        self, pattern: np.ndarray, steps: int = 10, synchronous: bool = False
    ) -> np.ndarray:
        """
        Recall a pattern by iteratively updating until convergence.

        Args:
            pattern (np.ndarray): The input pattern to recall.
            steps (int): Number of iterations to run for convergence.
            synchronous (bool): Whether to update neurons synchronously or asynchronously.

        Returns:
            np.ndarray: The recalled pattern.
        """
        pattern = pattern.copy()

        for _ in range(steps):
            pattern = self.update(pattern, synchronous)

        return pattern

    def find_spurious_states(
        self, patterns: List[np.ndarray], steps: int = 10
    ) -> List[np.ndarray]:
        """
        Find spurious states in the Hopfield network that are not part of the original patterns.

        Args:
            patterns (List[np.ndarray]): The list of original patterns.
            steps (int): Number of iterations to run for convergence in recall.

        Returns:
            List[np.ndarray]: List of spurious states found.
        """
        spurious_states = []
        original_patterns = set(tuple(pattern.flatten()) for pattern in patterns)

        # Generate all possible states
        for state in product([-1, 1], repeat=self.size):
            state = np.array(state)
            recalled_state = self.recall(state, steps)

            # If the recalled state is not an original pattern, consider it spurious
            if (
                tuple(recalled_state) not in original_patterns
                and tuple(recalled_state) not in spurious_states
            ):
                spurious_states.append(recalled_state)

        return spurious_states


# Example usage:
if __name__ == "__main__":
    size = 4  # Number of neurons
    patterns = [np.array([1, -1, 1, -1]), np.array([1, 1, -1, -1])]

    network = HopfieldNetwork(size)
    network.train(patterns)

    spurious_states = network.find_spurious_states(patterns)
    print("Spurious States:")
    for state in spurious_states:
        print(state)
