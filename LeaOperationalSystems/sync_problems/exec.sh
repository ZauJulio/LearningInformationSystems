red=`tput setaf 1`
green=`tput setaf 2`
magenta=`tput setaf 5`
reset=`tput sgr0`

echo -e "\n\t${green}Example: ${magenta}Binary Semaphore${reset}\n";
bin/binary_semaphore.c.bin

echo -e "\n\t${green}Example: ${magenta}Bounded Buffer${reset}\n";
bin/buffer.bin

echo -e "\n\t${green}Example: ${magenta}Readers-Writers${reset}\n";
bin/rw.bin

echo -e "\n\t${green}Example: ${magenta}Philosophers${reset}\n";
bin/philosophers.bin
