#include <stdio.h>

int main()
{
    int array[10] = {4, 1, 3, 5, 10, 8, 6, 9, 7, 2};

    int t, i, j;

    for (i = 1; i < 10; i++)
    {
        t = array[i];
        j = i - 1;

        while (j >= 0 && array[j] > t)
        {
            array[j + 1] = array[j];
            j = j - 1;
        }

        array[j + 1] = t;
    }

    for (i = 0; i < 10; i++)
    {
        printf("%d ", array[i]);
    }

    return 0;
}