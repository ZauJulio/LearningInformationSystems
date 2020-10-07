package main

import "fmt"

func main() {
	array := []int{4, 1, 3, 5, 10, 8, 6, 9, 7, 2}

	t := 0

	for i := 10; i > 0; i-- {

		for j := 1; j < i; j++ {

			if array[j-1] > array[j] {

				t = array[j]
				array[j] = array[j-1]
				array[j-1] = t
			}
		}
	}

	for i := 0; i < 10; i++ {
		fmt.Print(" ", array[i])
	}
}
