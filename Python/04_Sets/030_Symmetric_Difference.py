'''
COMMON SET OPERATIONS 
Using union(), intersection() and difference() functions.

>> a = {2, 4, 5, 9}
>> b = {2, 4, 11, 12}
>> a.union(b) # Values which exist in a or b
{2, 4, 5, 9, 11, 12}
>> a.intersection(b) # Values which exist in a and b
{2, 4}
>> a.difference(b) # Values which exist in a but not in b
{9, 5}

The union() and intersection() functions are symmetric methods:

>> a.union(b) == b.union(a)
True
>> a.intersection(b) == b.intersection(a)
True
>> a.difference(b) == b.difference(a)
False

TASK
Given 2 sets of integers, `M` and `N`, print their symmetric difference in 
ascending order. The term symmetric difference indicates those values that 
exist in either `M` or `N` but do not exist in both.
'''

if __name__ == '__main__':
    m = int(input())
    M = set(map(int, input().split()))
    n = int(input())
    N = set(map(int, input().split()))

    intersection = M.intersection(N)
    new_M = M - intersection
    new_N = N - intersection
    symm_diff = sorted(list(new_M.union(new_N)))
    
    for ii in symm_diff:
        print(ii)

