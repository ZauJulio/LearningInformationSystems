package main

import (
	"fmt"
	"os"
	"strconv"
)

func bubbleSort(array *[]int, size int) {
	/*  */

	for i := size; i > 0; i-- {

		for j := 1; j < i; j++ {

			if (*array)[j-1] > (*array)[j] {

				t := (*array)[j]
				(*array)[j] = (*array)[j-1]
				(*array)[j-1] = t
			}
		}
	}
}

func insertionSort(array *[]int, size int) {
	/*  */

	for i := 1; i < size; i++ {

		t := (*array)[i]
		j := i - 1

		for j >= 0 && (*array)[j] > t {

			(*array)[j+1] = (*array)[j]
			j = j - 1
		}

		(*array)[j+1] = t
	}
}

func selectionSort(array *[]int, size int) {
	/*  */

	for i := 0; i < size; i++ {

		for j := i + 1; j < size; j++ {

			if (*array)[j] < (*array)[i] {

				t := (*array)[j]
				(*array)[j] = (*array)[i]
				(*array)[i] = t
			}
		}
	}
}

func quickSort(a *[]int, left int, right int) {
	/*  */

	i := left
	j := right
	x := (*a)[(left+right)/2]

	for i <= j {

		for (*a)[i] < x && i < right {
			i++
		}

		for (*a)[j] > x && j > left {
			j--
		}

		if i <= j {
			t := (*a)[i]
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
	/*  */

	args := os.Args[2:]
	size := len(args)

	var array []int

	for i := 0; i < size; i++ {

		c, err := strconv.Atoi(args[i])

		if err == nil {
			array = append(array, c)
		}
	}

	if os.Args[1] == "bubbleSort" {
		bubbleSort(&array, size)
	} else {
		if os.Args[1] == "insertionSort" {
			insertionSort(&array, size)
		} else {
			if os.Args[1] == "selectionSort" {
				selectionSort(&array, size)
			} else {
				if os.Args[1] == "quickSort" {
					quickSort(&array, 0, size-1)
				} else {
					fmt.Println("USAGE  = exec [SORT] [a1 a2 a3 a4 aN]")
					fmt.Println("[SORT] = bubbleSort, selectionSort, insertionSort, quickSort.")
					fmt.Println("[a]    = int numbers separeted by spaces.")
					return
				}
			}
		}
	}

	for i := 0; i < size; i++ {
		fmt.Print(array[i], " ")
	}
}
