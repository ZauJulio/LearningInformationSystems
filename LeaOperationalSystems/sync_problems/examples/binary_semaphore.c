#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/types.h>
#include <unistd.h>

#include "../src/dijkstra.h"

key_t KEY = 123;

int main() {
    int sem = sem_create(KEY, 1);
    printf("A semaphore was created with the identifier %d\n", sem);

    if (fork() == 0) {
        printf("\x1B[32m\t> Child process uses the resource. \n\x1B[0m");
        P(sem);
        sleep(4);
        printf("\x1B[31m\t> Child process releases the resource. \n\x1B[0m");
        V(sem);
        sleep(1);
    } else {
        sleep(1);
        printf("\x1B[32mParent process blocks when trying to access the feature. \n\x1B[0m");
        P(sem);
        printf("\x1B[31mAvailable to the parent process. \n\x1B[0m");
        sem_delete(sem);
    }

    exit(0);
}