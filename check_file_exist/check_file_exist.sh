#!/bin/bash

# sh check_file_exist.sh
FILE="./a.txt"

if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
fi
