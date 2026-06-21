#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>

#include "../src/dijkstra.h"

static int PRODUCERS_NUM = 5;
static int BUFFER_SIZE = 5;

// General struct
struct arg_struct {
    int mutex;
    int full;
    int empty;
    int *buffer;
    int in;
    int out;
} * args;

// Producer struct
struct prod_struct {
    int id;
    struct arg_struct *arg;
} * producers;

void print_buffer(int *buffer) {
    printf("\n\t\x1B[32m== BUFFER ==\n\x1B[0m");
    for (int i = 0; i < BUFFER_SIZE; i++) printf("| %d ", buffer[i]);
    printf("|\n\n");
}

void *Producer(void *args) {
    struct prod_struct *producer_args = args;
    struct arg_struct *_args = producer_args->arg;
    int id = producer_args->id;
    int produto;

    usleep(rand() % 1000000);

    P(_args->empty); // Wait to empty consumers
    P(_args->mutex); // Lock the mutex

    printf("\x1B[33m> Producer %d has come into action!\n\x1B[0m", id);
    produto = rand() % 100;

    if (_args->buffer[_args->in] != -1) {
        printf("\t\x1B[33m==== PRODUCER ALERT %d ====\n\x1B[0m", id);
        printf("\t> Position %d was occupied with the value %d\n\n", _args->in, _args->buffer[_args->in]);
    }

    printf("\t\x1B[33m> Producer %d will record value %d in POS %d\n\x1B[0m", id, produto, _args->in);
    _args->buffer[_args->in] = produto;

    // Increase Buffer Position
    _args->in = (_args->in + 1) % BUFFER_SIZE;

    V(_args->mutex); // Unlock the mutex
    V(_args->full); // Notify consumers that the buffer is not empty

    return NULL;
}

void *Consumer(void *args) {
    struct arg_struct *_args = args;
    usleep(rand() % 1000000);

    int i = 0;

    while (i != PRODUCERS_NUM) {
        P(_args->full); // Wait producer
        P(_args->mutex); // Lock mutex
        printf("- Consumer came into action!\n");

        print_buffer(_args->buffer);
        if (_args->buffer[_args->out] == -1) {
            printf("\t\x1B[31m==== CONSUMER ALERT ====\n\x1B[0m");
            printf("\t> Position %d was empty\n\n", _args->in);
        }

        printf("\t- Consumed the value: %d\n", _args->buffer[_args->out]);

        // Cleaning
        _args->buffer[_args->out] = -1;
        _args->out = (_args->out + 1) % BUFFER_SIZE;

        V(_args->mutex); // Unlock mutex
        V(_args->empty); // Notify producer

        i++;
    }

    return NULL;
}

int main() {
    key_t key0 = 0, key1 = 1, key2 = 2;

    int mutex = sem_create(key0, 1);
    int full = sem_create(key1, 0);
    int empty = sem_create(key2, 5);
    int i, in = 0, out = 0;
    int *buffer;

    buffer = malloc(BUFFER_SIZE * sizeof(int));
    for (i = 0; i < BUFFER_SIZE; i++) buffer[i] = -1;

    args = malloc(sizeof(struct arg_struct) * 1);
    producers = malloc(sizeof(struct prod_struct) * PRODUCERS_NUM);

    args->mutex = mutex;
    args->full = full;
    args->empty = empty;
    args->buffer = buffer;
    args->in = in;
    args->out = out;

    pthread_t pID[PRODUCERS_NUM];
    pthread_t cID;

    srand(time(NULL));
    
    // Creates threads
    for (i = 0; i < PRODUCERS_NUM; i++) {
        producers[i].id = i;
        producers[i].arg = args;
        pthread_create(&pID[i], NULL, Producer, &producers[i]);
    }

    pthread_create(&cID, NULL, Consumer, args);

    // Waits for threads to finish
    for (i = 0; i < PRODUCERS_NUM; i++) pthread_join(pID[i], NULL);
    pthread_join(cID, NULL);

    // Delete sem's
    sem_delete(mutex);
    sem_delete(full);
    sem_delete(empty);

    free(buffer);
    free(args);
    free(producers);

    exit(0);
}