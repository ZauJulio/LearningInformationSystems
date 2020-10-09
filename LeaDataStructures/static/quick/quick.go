package main

import "fmt"

func quickSort(a *[]int, left int, right int) {
	i := left
	j := right
	x := (*a)[(left+right)/2]
	t := 0

	for i <= j {

		for (*a)[i] < x && i < right {
			i++
		}

		for (*a)[j] > x && j > left {
			j--
		}

		if i <= j {
			t = (*a)[i]
			(*a)[i] = (*a)[j]
			(*a)[j] = t
			i++
			j--
		}
	}

	if j > left {
		quickSort(a, left, j)
	}

	if i < right {
		quickSort(a, i, right)
	}
}

func main() {
	array := []int{4, 1, 3, 5, 10, 8, 6, 9, 7, 2}

	quickSort(&array, 0, 9)

	for i := 0; i < 10; i++ {
		fmt.Print(" ", array[i])
	}
}
