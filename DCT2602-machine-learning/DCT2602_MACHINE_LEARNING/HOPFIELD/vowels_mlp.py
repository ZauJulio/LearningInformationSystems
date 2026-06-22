import sys

sys.path.append("../")

import numpy as np
from data import vowels

from DCT2602_MACHINE_LEARNING.utils.mlp import MLP


def format_pattern(pattern: np.ndarray) -> np.ndarray:
    recalled_pattern = []

    for v in pattern:
        if v > 0:
            recalled_pattern.append("#")
        else:
            recalled_pattern.append(" ")

    return np.array(recalled_pattern).reshape(12, 10)


def binarize_data(x: np.ndarray) -> np.ndarray:
    return np.where(x > 0.5, 1, 0)


def main() -> None:
    vowel_patterns = np.array([*vowels.values()])
    vowel_labels = []

    for i in range(len(vowels)):
        label = [0] * len(vowels)
        label[i] = 1

        vowel_labels.append(label)

    vowel_labels = np.array(vowel_labels)

    X = vowel_patterns.reshape(len(vowel_patterns), -1)
    y = vowel_labels

    print(X, y)

    mlp = MLP(
        layer_sizes=[X.shape[1], 64, len(vowels)],
        learning_rate=0.01,
        epochs=50000,
        f="sigmoid",
        verbose=True,
    )
    mlp.train(X, y)

    predictions = binarize_data(mlp.predict(X))

    acc = np.mean(predictions == y)
    print(f"Accuracy: {acc}")

    # Change here to test different vowels, A: 0, ... , U: 4
    vowel_index = 1
    vowel_test = vowel_patterns[vowel_index].copy()
    pattern = binarize_data(mlp.predict(vowel_test.reshape(1, -1)[0]))

    original_vowel = [*vowels.keys()][vowel_index]
    predicted_vowel = [*vowels.keys()][np.argmax(pattern)]

    print(f"Original vowel X Predicted: {original_vowel} X {predicted_vowel}")
    print("Original vowel:   \n", format_pattern(vowel_test))
    print("Recovered vowel:   \n", format_pattern(vowel_patterns[vowel_index]))


if __name__ == "__main__":
    main()
