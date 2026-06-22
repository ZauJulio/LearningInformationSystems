#!/bin/bash

book="http://www.gutenberg.org/cache/epub/55752/pg55752.txt"
# Download book if file not exist
if [ ! -f "pg55752.txt" ]; then
  wget $book
fi

# Echo 15 words more cited in the book with more than 5 letters
cat pg55752.txt | tr -cs 'A-Za-z' ' ' | tr 'A-Z' 'a-z' | tr -s ' ' '\012' | sort | uniq -c | sort -rn | awk '{if (length($2) > 5) print $2}' | head -n 15
