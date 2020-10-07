package main

import "fmt"

func bubbleSort(array []int) []int {
	t := 0

	for i := len(array); i > 0; i-- {

		for i := 0; i < len(array)-1; i++ {

			if array[i] > array[i+1] {
		
				t = array[i+1]
				array[i+1] = array[i]
				array[i] = t
			}
		}
	}

	return array
}

func main() {
	array := []int{4, 1, 3, 5, 2, 8, 6, 9, 7, 10}
	fmt.Println(bubbleSort(array))
}
