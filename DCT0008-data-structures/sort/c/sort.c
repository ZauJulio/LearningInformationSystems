#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>

#include "src/insertionSort.c"
#include "src/mergeSort.c"
#include "src/quickSort.c"

void shuffle(int *A, int size);
void decreasing(int *A, int size);
int *allocate(int size);
int *copyArray(int *A, int size);
double orderArray(int *A, char *alg, char sourceOrder, int size);
void checkUsage(int argc);

void shuffle(int *A, int size) {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    int usec = tv.tv_usec;
    srand48(usec);

    if (size > 1) {
        for (int i = size - 1; i > 0; i--) {
            int j = (unsigned int)(drand48() * (i + 1));
            swap(&A[i], &A[j]);
        }
    }
}

void decreasing(int *A, int size) {
    for (int i = size, j = 0; i > 0; i--, j++) {
        A[j] = i;
    }
}

int *copyArray(int *A, int size) {
    int *B;
    B = (int *)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
        B[i] = A[i];
    }
    return B;
}

int *allocate(int size) {
    int *A;
    A = (int *)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
        A[i] = i;
    }
    return A;
}

double orderArray(int *A, char *alg, char sourceOrder, int size) {
    struct timeval begin, end;

    if (sourceOrder == 'r') {
        shuffle(A, size);
    }
    if (sourceOrder == 'd') {
        decreasing(A, size);
    }

    if (strcmp(alg, "mergeSort") == 0) {
        int *B = copyArray(A, size);
        gettimeofday(&begin, 0);
        mergeSort(A, B, 0, size - 1);
        gettimeofday(&end, 0);
        
        free(B);
    }
    if (strcmp(alg, "quickSort") == 0) {
        gettimeofday(&begin, 0);
        quickSort(A, 0, size - 1);
        gettimeofday(&end, 0);
    }
    if (strcmp(alg, "insertionSort") == 0) {
        gettimeofday(&begin, 0);
        insertionSort(A, size);
        gettimeofday(&end, 0);
    }

    long seconds = end.tv_sec - begin.tv_sec;
    long microseconds = end.tv_usec - begin.tv_usec;
    return seconds + microseconds*1e-6;;
}

void checkUsage(int argc) {
    if (argc < 6) {
        printf("\nIncorrect usage");
        printf("\n-------------------------------------------------\n");
        printf("USAGE: sort.so RANGE MAX_SIZE ORDER ALG MEAN_SIZE\n\n");
        printf("RANGE     => Array addition size\n");
        printf("MAX_SIZE  => Maximum size of arrays\n");
        printf("ORDER     => Initial ordering of the array:\n");
        printf("              (a) ordered\n");
        printf("              (d) inversely ordered\n");
        printf("              (r) randomly ordered\n\n");
        printf("ALG:      => sorting algorithm:\n");
        printf("              (mergeSort)\n");
        printf("              (quickSort)\n");
        printf("              (insertionSort)\n\n");
        printf("MEAN_SIZE => Sample run-time sample size for each\n");
        printf("             array size.\n\n");
        printf("Example: ./sort.so 100 1000 r quickSort 1000\n");
        printf("This averages 1000 different vectors, randomly ordered, with\n");
        printf("size starting from 100 to 1000, using the quickSort algorithm.\n");
        exit(0);
    }
}

int main(int argc, char *argv[]) {
    /*  */
    checkUsage(argc);

    int range = atoi(argv[1]);
    int maxSize = atoi(argv[2]) + range;
    char order = argv[3][0];
    char *alg = argv[4];
    int meanSize = atoi(argv[5]);

    double mean;
    int size = range;

    while (size < maxSize) {
        mean = 0;
        for (int i = 0; i < meanSize; i++) {
            int *A = allocate(size);
            double time_taken = orderArray(A, alg, order, size);
            free(A);
            mean += time_taken;
        }
        printf("%f %d\n", (double)mean/meanSize, size);
        size += range;
    }

    return 0;
}