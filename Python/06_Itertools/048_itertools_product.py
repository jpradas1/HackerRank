'''
itertools.product()

This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as:
    ((x,y) for x in A for y in B).

TASK
You are given a two lists `A` and `B`. Your task is to compute their cartesian 
product `A`X`B`
'''
from itertools import product

if __name__=='__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_cross_B = product(A,B)
    print(*list(A_cross_B))