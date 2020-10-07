package main

import "fmt"

func main() {
	array := []int{4, 1, 3, 5, 10, 8, 6, 9, 7, 2}

	t := 0

	for i := 0; i < 10; i++ {

		for j := i + 1; j < 10; j++ {

			if array[j] < array[i] {

				t = array[j]
				array[j] = array[i]
				array[i] = t
			}
		}
	}

	for i := 0; i < 10; i++ {
		fmt.Print(" ", array[i])
	}
}
