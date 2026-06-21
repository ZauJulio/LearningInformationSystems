#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>

#include "../src/dijkstra.h"

static int MAX_THREADS = 5;

struct arg_struct {
    int mutex;
    int wrt;
    int shared;
    int read_count;
} * args;

void *writer(void *args) {
    struct arg_struct *_args = args;

    P(_args->wrt);

    _args->shared = rand() % 100;
    printf("> Writer: shared = %d\n", _args->shared);

    V(_args->wrt);

    return NULL;
}

void *reader(void *args) {
    struct arg_struct *_args = args;

    P(_args->mutex);
    _args->read_count++;

    if (_args->read_count == 1)
        P(_args->wrt);

    printf("\t- Reader: shared = %d\n", _args->shared);

    _args->read_count--;

    if (_args->read_count == 0)
        V(_args->wrt);
    V(_args->mutex);

    return NULL;
}

int main() {
    key_t key0 = 0, key1 = 1;

    int mutex = sem_create(key0, 1);
    int wrt = sem_create(key1, 1);
    int read_count = 0;
    int shared = 0;
    int i;

    args = malloc(sizeof(struct arg_struct) * 1);

    args->mutex = mutex;
    args->wrt = wrt;
    args->shared = shared;
    args->read_count = read_count;

    pthread_t rID[MAX_THREADS];
    pthread_t wID[MAX_THREADS];

    // Creates threads
    for (i = 0; i < MAX_THREADS; i++) {
        pthread_create(&rID[i], NULL, reader, args);
        pthread_create(&wID[i], NULL, writer, args);
    }

    // Joins threads
    for (i = 0; i < MAX_THREADS; i++) {
        pthread_join(rID[i], NULL);
        pthread_join(wID[i], NULL);
    }

    // Delete sem's
    sem_delete(mutex);
    sem_delete(wrt);

    free(args);
    
    exit(0);
}