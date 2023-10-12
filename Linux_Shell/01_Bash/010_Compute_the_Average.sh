#!/bin/bash

# Given `N` integers, compute their average, rounded to three decimal places.

read N
ave=0

for ii in $(seq 1 $N)
do
    read num
    ave=$(($ave + $num))
done

printf "%.3f\n" $(echo "$ave/$N" | bc -l)