#!/bin/bash

# Get user and check if it is valid
read -p "Enter a user name: " user

# Check if user exists
if id -u $user > /dev/null 2>&1; then
    echo "User $user exists"
else
    echo "User $user does not exist"
    exit 1
fi