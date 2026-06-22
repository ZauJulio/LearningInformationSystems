#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>

#include "../src/dijkstra.h"

static int PHILO_NUM = 5;

// General struct
struct arg_struct {
    int *mutex_chopstick;
    int *chopstick_use;
} * args;

// Philosopher struct
struct philo_struct {
    int id;
    struct arg_struct *args;
} * philosophers;

void *Philosopher(void *philo_args) {
    struct philo_struct *philosopher_args = philo_args;
    struct arg_struct *_args = philosopher_args->args;
    int id = philosopher_args->id;
    int c1, c2;

    usleep(rand() % 1000000);

    if (id % 2 == 0) {
        c1 = id;                    // left
        c2 = (id + 1) % PHILO_NUM;  // right
    } else {
        c1 = (id + 1) % PHILO_NUM;  // right
        c2 = id;                    // left
    }

    // Wait for chopsticks
    P(_args->mutex_chopstick[c1]);
    P(_args->mutex_chopstick[c2]);

    if (_args->chopstick_use[c1] != -1) printf("\x1B[33mALERT: chopstick %d being used by %d\n\x1B[0m", c1, _args->chopstick_use[c1]);
    if (_args->chopstick_use[c2] != -1) printf("\x1B[33mALERT: chopstick %d being used by %d\n\x1B[0m", c2, _args->chopstick_use[c2]);

    _args->chopstick_use[c1] = id;
    _args->chopstick_use[c2] = id;

    printf("\x1B[32m+ Filosofo %d pegou o chopstick [%d] e [%d]\x1B[0m\n", id, c1, c2);

    printf("\t> Filosofo %d comendo\n", id);
    usleep(rand() % 1000000);

    _args->chopstick_use[c1] = -1;
    _args->chopstick_use[c2] = -1;
    printf("\x1B[31m- Filosofo %d liberou o chopstick [%d] e [%d]\x1B[0m\n", id, c1, c2);

    // Signal chopsticks
    V(_args->mutex_chopstick[c1]);
    V(_args->mutex_chopstick[c2]);

    return NULL;
}

int main() {
    pthread_t pID[PHILO_NUM];
    int *chopstick_use = malloc(sizeof(int) * PHILO_NUM);
    int *mutex_chopstick = malloc(sizeof(int) * PHILO_NUM);
    int i;

    args = malloc(sizeof(struct arg_struct) * 1);
    philosophers = malloc(sizeof(struct philo_struct) * PHILO_NUM);

    // Initialize chopsticks and sem's
    for (i = 0; i < PHILO_NUM; i++) {
        chopstick_use[i] = -1;
        mutex_chopstick[i] = sem_create(i, 1);
    }

    args->mutex_chopstick = mutex_chopstick;
    args->chopstick_use = chopstick_use;

    srand(time(NULL));

    // Creates threads
    for (i = 0; i < PHILO_NUM; i++) {
        philosophers[i].id = i;
        philosophers[i].args = args;
        pthread_create(&pID[i], NULL, Philosopher, &philosophers[i]);
    }

    // Waits for threads to finish
    for (i = 0; i < PHILO_NUM; i++) pthread_join(pID[i], NULL);
    
    // Delete sem's
    for (i = 0; i < PHILO_NUM; i++) sem_delete(mutex_chopstick[i]);

    free(chopstick_use);
    free(mutex_chopstick);
    free(philosophers);
    free(args);

    exit(0);
}