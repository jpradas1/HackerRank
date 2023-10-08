'''
You are given a set `A` and `n` other sets.
Your job is to find whether set `A` is a strict superset of each of 
the `N` sets.

Print True, if `A` is a strict superset of each of the `N` sets. 
Otherwise, print False.

A strict superset has at least one element that does not exist in its 
subset.
'''

if __name__ == '__main__':
    A = set(map(int, input().split()))
    n = int(input())
    flag = True

    for _ in range(n):
        N = set(map(int, input().split()))
        if N.intersection(A) != N or N == A:
            flag = False
            break

    print(flag)