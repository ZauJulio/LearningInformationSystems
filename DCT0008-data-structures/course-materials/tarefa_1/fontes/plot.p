set term eps
set key right bottom
set output 'images/random-order.eps'
set title 'Entrada Aleatoriamente Ordenada'
plot "graficos/random/insertionSort" with lines title 'Insertion Sort',  "graficos/random/mergeSort" with lines title 'Merge Sort', "graficos/random/quickSort" with lines title 'Quick Sort'

set output 'images/pre-order.eps'
set title 'Entrada Ordenada'
plot "graficos/ascendant/insertionSort" with lines title 'Insertion Sort',  "graficos/ascendant/mergeSort" with lines title 'Merge Sort', "graficos/ascendant/quickSort" with lines title 'Quick Sort'

set output 'images/reverse-order.eps'
set title 'Entrada Inversamente Ordenada'
plot "graficos/reverse/insertionSort" with lines title 'Insertion Sort',  "graficos/reverse/mergeSort" with lines title 'Merge Sort', "graficos/reverse/quickSort" with lines title 'Quick Sort'

set output 'images/insertion-sort.eps'
set title 'Insertion Sort'
plot "graficos/random/insertionSort" with lines title 'Entrada Aleatoriamente Ordenada', "graficos/ascendant/insertionSort" with lines title 'Entrada Ordenada', "graficos/reverse/insertionSort" with lines title 'Entrada Inversamente Ordenada'

set output 'images/merge-sort.eps'
set title 'Merge Sort'
plot "graficos/random/mergeSort" with lines title 'Entrada Aleatoriamente Ordenada', "graficos/ascendant/mergeSort" with lines title 'Entrada Ordenada', "graficos/reverse/mergeSort" with lines title 'Entrada Inversamente Ordenada'

set output 'images/quick-sort.eps'
set title 'Quick Sort'
plot "graficos/random/quickSort" with lines title 'Entrada Aleatoriamente Ordenada', "graficos/ascendant/quickSort" with lines title 'Entrada Ordenada', "graficos/reverse/quickSort" with lines title 'Entrada Inversamente Ordenada'

set output 'images/def_insertion-sort.eps'
set title 'Insertion Sort'
plot "graficos/random/insertionSort" with lines title 'Insertion Sort'

set output 'images/def_merge-sort.eps'
set title 'Merge Sort'
plot "graficos/random/mergeSort" with lines title 'Merge Sort'

set output 'images/def_quick-sort.eps'
set title 'Quick Sort'
plot "graficos/random/quickSort" with lines title 'Quick Sort'