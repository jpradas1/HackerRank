#!/bin/bash

# Read in one character from STDIN.
# If the character is 'Y' or 'y' display "YES".
# If the character is 'N' or 'n' display "NO".
# No other character will be provided as input.

read ch

if [ $ch == "y" ] || [ $ch == "Y" ]; then
    echo "YES"
elif [ $ch == "n" ] || [ $ch == "N" ]; then
    echo "NO"
fi