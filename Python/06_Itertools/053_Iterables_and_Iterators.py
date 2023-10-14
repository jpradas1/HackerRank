'''
The itertools module standardizes a core set of fast, memory efficient 
tools that are useful by themselves or in combination. Together, they form 
an iterator algebra making it possible to construct specialized tools 
succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their 
documentation here.
    https://docs.python.org/3/library/itertools.html

You are given a list of `N` lowercase English letters. For a given integer `K`,
you can select any `K` indices (assume 1-based indexing) with a uniform 
probability from the list.

Find the probability that at least one of the `K` indices selected will 
contain the letter: 'a'.
'''
import itertools as iter

if __name__=='__main__':
    N = int(input())
    chain = list(map(str,input().split()))
    K = int(input())

    comb = list(iter.combinations(chain,K))
    filter_comb = list(iter.filterfalse(lambda x: 'a' in x, comb))

    prob_a = 1 - len(filter_comb)/len(comb)
    print('{:.3f}'.format(prob_a))