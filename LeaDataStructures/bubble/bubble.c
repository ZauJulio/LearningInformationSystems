#include <stdio.h>

int main()
{
    int array[10] = {4, 1, 3, 5, 10, 8, 6, 9, 7, 2};

    int t = 0;
    int i = 10;
    int j = 1;

    for (i; i > 0; i--)
    {
        
        for (j = 1; j < i; j++)
        {
            if (array[j - 1] > array[j])
            {
                t = array[j];
                array[j] = array[j - 1];
                array[j - 1] = t;
            }
        }
    }

    for (i = 0; i < 10; i++)
    {
        printf("%d ", array[i]);
    }

    return 0;
}