#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void bubbleSort(int *array, int size);
void selectionSort(int *array, int size);
void insertionSort(int *array, int size);
void quickSort(int *array, int left, int right);

void bubbleSort(int *array, int size) {
    /*  */

    int t, j;

    for (int i = size; i > 0; i--) {
        for (j = 1; j < i; j++) {
            if (array[j - 1] > array[j]) {
                t = array[j];
                array[j] = array[j - 1];
                array[j - 1] = t;
            }
        }
    }
}

void selectionSort(int *array, int size) {
    /*  */

    int t, j;

    for (int i = 0; i < size; i++) {
        for (j = i + 1; j < size; j++) {
            if (array[j] < array[i]) {
                t = array[j];
                array[j] = array[i];
                array[i] = t;
            }
        }
    }
}

void insertionSort(int *array, int size) {
    /*  */
    int t, j;

    for (int i = 1; i < size; i++) {
        t = array[i];
        j = i - 1;

        while (j >= 0 && array[j] > t) {
            array[j + 1] = array[j];
            j = j - 1;
        }

        array[j + 1] = t;
    }
}

void quickSort(int *array, int left, int right) {
    /*  */

    int i, j, x, t;

    i = left;
    j = right;
    x = array[(left + right) / 2];

    while (i <= j) {
        while (array[i] < x && i < right) {
            i++;
        }

        while (array[j] > x && j > left) {
            j--;
        }

        if (i <= j) {
            t = array[i];
            array[i] = array[j];
            array[j] = t;
            i++;
            j--;
        }
    }

    if (j > left) {
        quickSort(array, left, j);
    }
    if (i < right) {
        quickSort(array, i, right);
    }
}

int main(int argc, char *argv[]) {
    /*  */
    int *array;
    array = malloc((argc - 2) * sizeof(int));

    for (int i = 2, k = 0; i < argc; i++, k++) {
        array[k] = atoi(argv[i]);
    }

    // Switch sort's
    if (strcmp(argv[1], "bubbleSort") == 0) {
        bubbleSort(array, argc - 1);
    } else {
        if (strcmp(argv[1], "selectionSort") == 0) {
            selectionSort(array, argc - 1);
        } else {
            if (strcmp(argv[1], "insertionSort") == 0) {
                insertionSort(array, argc - 1);
            } else {
                if (strcmp(argv[1], "quickSort") == 0) {
                    quickSort(array, 0, argc - 2);
                } else {
                    printf("USAGE  = exec [SORT] [a1 a2 a3 a4 aN]\n");
                    printf("[SORT] = bubbleSort, selectionSort, insertionSort, quickSort.\n");
                    printf("[a]    = int numbers separeted by spaces.\n");

                    return 0;
                }
            }
        }
    }

    // STD output
    for (int i = 0; i < argc - 2; i++) {
        printf("%d ", array[i]);
    }
    return 0;
}