#!/bin/bash

read N
unders=""

blank_lines_row=63

for ii in $(seq 1 $N); do blank_lines_row=$(($blank_lines_row - 2**(6-$ii))); done

# line in blank
for ii in $(seq 1 100); do unders+='_';done

# first lines in blank
for jj in $(seq 1 $blank_lines_row); do echo "$unders"; done


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

for ii in $(seq 0 $((N-1))); do echo "$(n_base $(($N-$ii)))"; done



# # node 1
# limit1=$(( 2**(5-$N) ))
# for nn in $(seq 1 $limit1)
# do
#     node1=''
#     for ii in $(seq 1 $(($initial_position-$limit1+$nn-1))); do node1+='_'; done
#     node1+='1'
#     for ii in $(seq 1 $((($limit1+1-$nn)*2-1))); do node1+='_'; done
#     node1+='1'
#     for ii in $(seq 1 $(($initial_position-$limit1+$nn))); do node1+='_'; done
#     echo "$node1"
# done