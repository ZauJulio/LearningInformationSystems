import sys

sys.path.append("../")

import numpy as np
from data import vowels

from DCT2602_MACHINE_LEARNING.HOPFIELD.hopfield import HopfieldNetwork


def format_pattern(pattern: np.ndarray) -> np.ndarray:
    recalled_pattern = []

    for v in pattern:
        if v > 0:
            recalled_pattern.append("#")
        else:
            recalled_pattern.append(" ")

    return np.array(recalled_pattern).reshape(12, 10)


def binarize_data(x: np.ndarray) -> np.ndarray:
    return np.where(x == -1, 0, 1)


def main() -> None:
    vowel_patterns = [*vowels.values()]

    network = HopfieldNetwork(size=120)
    network.train(vowel_patterns)

    corrupted_pattern = vowel_patterns[2].copy()

    for _ in range(10):
        pos = np.random.randint(0, 120)

        if corrupted_pattern[pos] == -1:
            corrupted_pattern[pos] = 1
        else:
            corrupted_pattern[pos] = -1

    recalled_pattern = format_pattern(network.recall(corrupted_pattern, steps=100))

    print("Corrupted vowel:   \n", format_pattern(corrupted_pattern))
    print("Recovered vowel:   \n", recalled_pattern)


if __name__ == "__main__":
    main()
