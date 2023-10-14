'''
itertools.permutations(iterable[, r])

This tool returns successive `r` length permutations of elements in an 
iterable.

If `r` is not specified or is None, then `r` defaults to the length of the 
iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input 
iterable is sorted, the permutation tuples will be produced in a sorted 
order.

TASK
You are given a string `S`.
Your task is to print all possible permutations of size `k` of the string 
in lexicographic sorted order.
'''

from itertools import permutations

if __name__=='__main__':
    chain, num = map(str,input().split())
    result = sorted(list(permutations(chain,int(num))))
    for ii in result:
        print(''.join(ii))