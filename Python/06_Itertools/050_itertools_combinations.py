'''
itertools.combinations(iterable, r)
This tool returns the `r` length subsequences of elements from the input 
iterable.

Combinations are emitted in lexicographic sorted order. So, if the input 
iterable is sorted, the combination tuples will be produced in sorted order.

TASK
You are given a string `S`.
Your task is to print all possible combinations, up to size `k`, of the 
string in lexicographic sorted order.
'''

from itertools import combinations

if __name__=='__main__':
    chain, num = map(str,input().split())
    for kk in range(1,int(num)+1):
        result = list(combinations(chain, kk))
        result = sorted([sorted(x) for x in result])
        for ii in result:
            print(''.join(ii))