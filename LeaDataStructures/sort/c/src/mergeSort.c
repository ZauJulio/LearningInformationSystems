void mergeSort(int A[], int B[], int s, int e);
void merge(int A[], int B[], int s, int m, int e);

void mergeSort(int A[], int B[], int s, int e) {
    if (s < e) {
        int m = (s + e) / 2;
        mergeSort(A, B, s, m);
        mergeSort(A, B, m + 1, e);
        merge(A, B, s, m, e);
    }
}

void merge(int A[], int B[], int s, int m, int e) {
    int i = s;
    int j = m + 1;
    for (int k = 0; k < (e - s + 1); k++) {
        if ((A[i] < A[j] && i <= m) || j > e) {
            B[k] = A[i];
            i++;
        } else {
            B[k] = A[j];
            j++;
        }
    }
    for (int k = 0; k < (e - s + 1); k++) {
        A[s + k] = B[k];
    }
}