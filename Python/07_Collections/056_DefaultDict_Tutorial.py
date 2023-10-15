'''
The defaultdict tool is a container in the collections class of Python. 
It's similar to the usual dictionary (dict) container, but the only 
difference is that a defaultdict will have a default value if that key has 
not been set yet. If you didn't use a defaultdict you'd have to check to 
see if that key exists, and if it doesn't, set it to what you want.

In this challenge, you will be given 2 integers, `n` and `m`. There are `n` 
words, which might repeat, in word group `A`. There are `m` words belonging 
to word group `B`. For each `m` words, check whether the word has appeared 
in group `A` or not. Print the indices of each occurrence of `m` in group 
`A`. If it does not appear, print `-1`.
'''

from collections import defaultdict

if __name__=='__main__':
    n, m = map(int, input().split())
    dct = defaultdict(list)

    for _ in range(n):
        dct['A'].append(input())
    for _ in range(m):
        dct['B'].append(input())

    for bb in dct['B']:
        if bb in dct['A']:
            pos = [ii+1 for ii, aa in enumerate(dct['A']) if bb==aa]
            print(*pos)
        else:
            print(-1)