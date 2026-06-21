# Simple binary semaphore
gcc -Wall examples/binary_semaphore.c -o bin/binary_semaphore.bin

# Bounded buffer
gcc -pthread -Wall examples/buffer.c -o bin/buffer.bin

# Readers-Writers
gcc -pthread -Wall examples/rw.c -o bin/rw.bin

# Philosophers
gcc -pthread -Wall examples/philosophers.c -o bin/philosophers.bin