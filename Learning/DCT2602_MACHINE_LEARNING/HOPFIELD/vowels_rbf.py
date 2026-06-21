import sys

import numpy as np

sys.path.append("../")

from data import vowels

from DCT2602_MACHINE_LEARNING.utils.kmeans import KMeans
from DCT2602_MACHINE_LEARNING.utils.rbf import RBFNetwork


def format_pattern(pattern: np.ndarray):
    recalled_pattern = []

    for v in pattern:
        if v > 0:
            recalled_pattern.append("#")
        else:
            recalled_pattern.append(" ")

    return np.array(recalled_pattern).reshape(12, 10)


def binarize_data(x: np.ndarray):
    return np.where(x > 0.5, 1, 0)


def main() -> None:
    X = np.array(list(vowels.values()))
    y = np.array([0, 1, 2, 3, 4])

    kmeans = KMeans(k=5)
    centroids, _ = kmeans.fit(X)

    rbf_network = RBFNetwork(
        centers=centroids,
        sigma=1.0,
    )

    rbf_network.fit(X, y)

    if len(sys.argv) > 1:
        try:
            test_index = int(sys.argv[1])

            if test_index < 0 or test_index >= len(X):
                return print(
                    f"Index {test_index} is out of range. Please use a value between 0 and {len(X) - 1}."
                )
        except ValueError:
            return print("Please provide a valid integer index.")
    else:
        test_index = np.random.randint(len(X))

    test_x = X[test_index].reshape(1, -1)
    test_y = y[test_index]

    predicted_class = int(np.round(rbf_network.predict(test_x))[0])

    print(f"Testing vowel at index {test_index}:")
    print(f"Expected class: {test_y}")
    print(f"Predicted class: {predicted_class}")

    print("Formatted input pattern: \n", format_pattern(test_x.flatten()))

    predicted_classes = np.round(rbf_network.predict(X)).astype(int)
    accuracy = np.mean(predicted_classes == y) * 100
    print(f"Overall accuracy: {accuracy:.2f}%")


if __name__ == "__main__":
    main()
