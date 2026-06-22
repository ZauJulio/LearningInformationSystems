#!/bin/bash

dir=$1
count=0

for file in $dir/*; do
  if [ -f "$file" ]; then
    count=$((count + 1))

    name=$(basename "$file")
    name="${name%.*}"
    name=$(echo "$name" | tr '[:lower:]' '[:upper:]')

    ext="${file##*.}"
    ext=$(echo "$ext" | tr '[:lower:]' '[:upper:]')

    echo "$name$count.$ext"
  fi
done
