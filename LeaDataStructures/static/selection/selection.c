#include <stdio.h>

int main()
{
    int array[10] = {4, 1, 3, 5, 10, 8, 6, 9, 7, 2};

    int t = 0;
    int i = 0;
    int j = 0;

    for (i; i < 10; i++)
    {
        
        for (j = i+1; j < 10; j++)
        {
            if (array[j] < array[i])
            {
                t = array[j];
                array[j] = array[i];
                array[i] = t;
            }
        }
    }

    for (i = 0; i < 10; i++)
    {
        printf("%d ", array[i]);
    }

    return 0;
}