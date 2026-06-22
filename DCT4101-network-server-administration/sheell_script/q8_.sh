#!/bin/bash

dir="/home/$USER/foca"

mkdir -p $dir
cd $dir

file="https://www.guiafoca.org/download/static/inic/focalinux-1-html.tar.gz"

if [ ! -f "focalinux-1-html.tar.gz" ]; then
  wget $file
fi

if [ ! -f "index.html" ]; then
  tar -xvf focalinux-1-html.tar.gz
fi

word_search=$1
chapter="ch$2.html"

text=$(cat $chapter | tr -cs 'A-Za-z' ' ' | tr 'A-Z' 'a-z' | tr -s ' ' '\012' | sort)

echo $text | grep -o $word_search | wc -l
