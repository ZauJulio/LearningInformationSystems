import numpy as np
from typing import Tuple


class KMeans:
    def __init__(self, k: int, max_iters: int = 100, tol: float = 1e-4):
        """
        Initialize the KMeans class.

        Args:
            k (int): Number of clusters.
            max_iters (int, optional): Maximum number of iterations. Defaults to 100.
            tol (float, optional): Tolerance for convergence. Defaults to 1e-4.
        """
        self.k: int = k
        self.max_iters: int = max_iters
        self.tol: float = tol
        
        self.centroids: np.ndarray = np.array([])
        self.clusters: np.ndarray = np.array([])

    def initialize_centroids(self, X: np.ndarray) -> None:
        """
        Initialize centroids randomly from the dataset.

        Args:
            X (np.ndarray): Data points of shape (n_samples, n_features).
        """
        indices = np.random.choice(X.shape[0], self.k, replace=False)
        self.centroids = X[indices]

    def assign_clusters(self, X: np.ndarray) -> np.ndarray:
        """
        Assign each data point to the closest centroid.

        Args:
            X (np.ndarray): Data points of shape (n_samples, n_features).

        Returns:
            np.ndarray: Array of cluster assignments of shape (n_samples,).
        """
        # Calculate the distance from each point to each centroid
        distances = np.sqrt(((X - self.centroids[:, np.newaxis]) ** 2).sum(axis=2))
        clusters = np.argmin(distances, axis=0)

        return clusters

    def update_centroids(self, X: np.ndarray, clusters: np.ndarray) -> np.ndarray:
        """
        Update the centroids by calculating the mean of all points assigned to each centroid.

        Args:
            X (np.ndarray): Data points of shape (n_samples, n_features).
            clusters (np.ndarray): Array of cluster assignments of shape (n_samples,).

        Returns:
            np.ndarray: Updated centroids of shape (k, n_features).
        """
        new_centroids = np.array([X[clusters == i].mean(axis=0) for i in range(self.k)])

        return new_centroids

    def fit(self, X: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Fit the KMeans model to the data.

        Args:
            X (np.ndarray): Data points of shape (n_samples, n_features).

        Returns:
            Tuple[np.ndarray, np.ndarray]: Final centroids of shape (k, n_features)
                                           and cluster assignments of shape (n_samples,).
        """
        self.initialize_centroids(X)

        for i in range(self.max_iters):
            self.clusters = self.assign_clusters(X)
            new_centroids = self.update_centroids(X, self.clusters)

            # Check for convergence
            if np.all(np.abs(new_centroids - self.centroids) < self.tol):
                break

            self.centroids = new_centroids

        return self.centroids, self.clusters
