package src.mergeSort


func mergeSort(A *int, B *int, s int, e int) {
	if s < e {
		var m int = (s + e) / int(2)
		mergeSort(A, B, s, m)
		mergeSort(A, B, m+int(1), e)
		merge(A, B, s, m, e)
	}
}

func merge(A *int, B *int, s int, m int, e int) {
	var i := s
	var j := m + 1
	for k:= 0; k < e-s+1; k++ {
		if ((A[i] < A[j] && i <= m) || j > e) {
			B[k] = A[i]
			i++
		} else {
			B[k] = A[j]
			j++
		}
	}
	for k := 0; k < e-s+int(1); k++ {
		A[s + k] = B[k]
	}
}
