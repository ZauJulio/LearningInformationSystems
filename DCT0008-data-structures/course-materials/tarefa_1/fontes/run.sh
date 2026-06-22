#!/bin/bash

# Compile library
make

# Calculate execution time of the algorithms for a randomly ordered array
./sort.so 100 1000 r quickSort 1000 > graficos/random/quickSort
./sort.so 100 1000 r insertionSort 1000 > graficos/random/insertionSort
./sort.so 100 1000 r mergeSort 1000 > graficos/random/mergeSort

# Calculate execution time of the algorithms for an ordered array
./sort.so 100 1000 a quickSort 1000 > graficos/ascendant/quickSort
./sort.so 100 1000 a insertionSort 1000 > graficos/ascendantinsertionSort
./sort.so 100 1000 a mergeSort 1000 > graficos/ascendant/mergeSort

# Calculate execution time of the algorithms for an inversely ordered array
./sort.so 100 1000 d quickSort 1000 > graficos/reverse/quickSort
./sort.so 100 1000 d insertionSort 1000 > graficos/reverse/insertionSort
./sort.so 100 1000 d mergeSort 1000 > graficos/reverse/mergeSort

# Generate graphics in eps
gnuplot plot.p