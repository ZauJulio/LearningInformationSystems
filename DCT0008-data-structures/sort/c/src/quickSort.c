void quickSort(int *A, int s, int e);
int partition(int *A, int s, int e);
void swap(int *a, int *b);

void quickSort(int *A, int s, int e) {
    if (s < e) {
        int p = partition(A, s, e);
        quickSort(A, s, p - 1);
        quickSort(A, p + 1, e);
    }
}

int partition(int *A, int s, int e) {
    int k = A[e];
    int i = s - 1;
    for (int j = s; j < e; j++) {
        if (A[j] < k) {
            i++;
            swap(&A[i], &A[j]);
        }
    }
    swap(&A[i + 1], &A[e]);
    return i + 1;
}

void swap(int *a, int *b) {
    int t;

    t = *b;
    *b = *a;
    *a = t;
}