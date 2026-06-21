package src.quickSort

func quickSort(A *int, s int, e int) {
	if s < e {
		var p int = partition(A, s, e)
		quickSort(A, s, p-1)
		quickSort(A, p+1, e)
	}
}

func partition(A *int, s int, e int) int {
	var k int = A[e]
	var i int = s - 1
	for j:= s; j < e; j++ {
		if (A[j] < k) {
			i += 1
			swap(&A[i], &A[j])
		}
	}
	swap(&A[i + 1], &A[e])
	return i + 1
}

func swap(a *int, b *int) {
	var t := *b
	*b = *a
	*a = t
}
