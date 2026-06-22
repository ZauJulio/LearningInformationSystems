#!/bin/bash

clear

echo

echo -e "::Show::"
echo -e "1 - Display status of the use of system partitions."
echo -e "2 - Logged users."
echo -e "3 - Date/hour."
echo -e "4 - Quit"

echo
read -p "Enter your option: " option

case $option in
1)
  # Echo status of system partitions
  echo "$(df -h)"
  ;;
2)
  echo "$(who)"
  ;;
3)
  echo "$(date)"
  ;;
4)
  exit 0
  ;;
*)
  clear
  echo "Invalid option"
  ;;
esac
