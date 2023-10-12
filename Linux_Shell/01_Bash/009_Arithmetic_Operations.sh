#!/bin/bash

# A mathematical expression containing +,-,*,^, / and parenthesis will be 
# provided. Read in the expression, then evaluate it. Display the result 
# rounded to 3 decimal places.

read X

printf "%.3f\n" $(echo "$X" | bc -l)
# echo $(printf "%.3f\n"  $(echo " scale=4; $X" |bc))