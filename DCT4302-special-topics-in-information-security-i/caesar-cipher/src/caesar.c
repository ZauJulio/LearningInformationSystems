#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

#define NUM_LETTERS 26
#define SIZE 256
#define USAGE                                               \
    "Caesar Cipher based encryption and decryption tool.\n" \
    "The result is printed to standard output.\n\n"         \
    "%s <key> <file>\n"                                     \
    "  <key>  - Key used to encrypt or decrypt.\n"          \
    "  <file> - File to encrypt or decrypt.\n"

void decrypt(const char* filename, int k);
void count_chars(const char* filename);

int main(int argc, char** argv) {
    char c, e;
    FILE* f;

    if (argc == 2) {
        count_chars(argv[1]);

        for (int i = 0; i < SIZE; i++) {
            decrypt(argv[1], i);
        }
    } else if (argc == 3) {
        int k = atoi(argv[2]);

        decrypt(argv[1], k);
    } else {
        printf(USAGE, argv[0]);
    }

    return 0;
}

void decrypt(const char* filename, int k) {
    FILE* f;
    char c, e;

    f = fopen(filename, "r");

    if (f) {
        while (fread(&c, 1, 1, f)) {
            e = (c + k) % SIZE;
            if (e < 0)
                e = SIZE + e;
            printf("%c", e);
        }
    }
}

void count_chars(const char* filename) {
    int count[NUM_LETTERS] = {0};
    int c;

    FILE* fp = fopen(filename, "r");

    while ((c = fgetc(fp)) != EOF) {
        if (isalpha(c)) {
            c = toupper(c);
            count[c - 'A']++;
        }
    }

    fclose(fp);

    // Find the 10 most frequent characters
    for (int i = 0; i < 20; i++) {
        int max_count = 0;
        int max_index = 0;

        for (int j = 0; j < NUM_LETTERS; j++) {
            if (count[j] > max_count) {
                max_count = count[j];
                max_index = j;
            }
        }

        if (max_count == 0) {
            break;
        }

        printf("%c: %d\n", 'A' + max_index, max_count);
        count[max_index] = 0;
    }
}