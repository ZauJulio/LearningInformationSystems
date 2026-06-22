package src.insertionSort

func insertionSort(A *int, size int) {
	var i int, j int, k int
	for j = 1; j < size; j++ {
		k = A[j]
		i = j - 1
		for i >= 0 && A[i] > k {
			A[i + 1] = A[i]
			i--
		}
		A[i + 1] = k
	}
}
