'''
itertools.combinations_with_replacement(iterable, r)

This tool returns `r` length subsequences of elements from the input 
iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input 
iterable is sorted, the combination tuples will be produced in sorted order.

TASK
You are given a string `S`.
Your task is to print all possible size `k`  replacement combinations of the 
string in lexicographic sorted order.
'''

from itertools import combinations_with_replacement

if __name__=='__main__':
    chain, num = map(str,input().split())
    result = list(combinations_with_replacement(chain, int(num)))
    result = sorted([sorted(x) for x in result])
    
    for ii in result:
        print(''.join(ii))