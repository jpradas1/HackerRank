#!/bin/bash

# Creating a Fractal Tree from Y-shaped branches

# This challenge involves the construction of trees, in the form of ASCII 
# Art.

# We have to deal with real world constraints, so we cannot keep repeating 
# the pattern infinitely. So, we will provide you a number of iterations, 
# and you need to generate the ASCII version of the Fractal Tree for only 
# those many iterations (or, levels of recursion). A few samples are 
# provided below.

read N

# first lines in blank
blank_lines_row=63
for ii in $(seq 1 $N); do blank_lines_row=$(($blank_lines_row - 2**(6-$ii))); done

unders=""
for ii in $(seq 1 100); do unders+='_';done

for jj in $(seq 1 $blank_lines_row); do echo "$unders"; done

# fractal base
n_base() {
    base_line=19
    for ii in $(seq 1 $((5-$1))); do base_line=$(($base_line+2**($ii) )); done

    rows=$((2**(5-$1)))
    node=''
    for ii in $(seq 1 $base_line); do node+='_'; done

    for jj in $(seq 1 $((2**($1-1)-1)))
    do
        node+='1'
        for ii in $(seq 1 $((4*$rows-1))); do node+='_'; done
    done

    node+='1'
    for ii in $(seq 1 $(($base_line+1))); do node+='_'; done

    for jj in $(seq 1 $rows); do echo "$node"; done
}

# fractal branches
slide_branch() {
    line='1'
    for ii in $(seq 1 $((2*$1+1))); do line+='_'; done
    line+='1'
    echo "$line"
}

branchs() {
    base_line=18
    for ii in $(seq 0 $((4-$1))); do base_line=$(($base_line+2**($ii))); done
    # echo "$base_line"

    rows=$((2**(5-$1)))
    for ii in $(seq 1 $rows)
    do
        line=''
        for kk in $(seq 1 $base_line); do line+='_'; done

        for kk in $(seq 1 $((2**($1-1)-1)))
        do 
            line+=$(slide_branch $(($rows-$ii)))
            limit=$((4*$rows-2*($rows-ii+1)-1))
            for nn in $(seq 1 $limit); do line+='_'; done
        done

        line+=$(slide_branch $(($rows-$ii)))
        for kk in $(seq 1 $(($base_line+1))); do line+='_'; done
        base_line=$(($base_line+1))
        echo "$line"
    done
}

for ii in $(seq 0 $((N-1)))
do 
    echo "$(branchs $(($N-$ii)))"
    echo "$(n_base $(($N-$ii)))"
done