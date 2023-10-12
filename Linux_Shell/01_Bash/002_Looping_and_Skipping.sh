#!/bin/bash

# Your task is to use for loops to display only odd natural numbers 
# from 1 to 99.

for ii in {1..99}
do
    if [ $(expr $ii % 2) != "0" ]; then
        echo "$ii"
    fi
done