#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


char * cat(char *args[], int size) {
    /*  */

    char *string = malloc(1000 * sizeof(char));

    for (int i = 0; i < size - 1; i++) {
        strcat(string, args[i + 1]);
        strcat(string, " ");
        strcat(string, "\0");
    }

    return string;
}


int main(int argc, char *argv[]) {
    /*  */
    
    char *args;
    args = cat(argv, argc);
    
    clock_t tic = clock();
    
    int status = system(args);

    clock_t tac = clock();

    printf("\n%f\n", (double)(tac - tic) / CLOCKS_PER_SEC);

    free(args);
    return 0;
}