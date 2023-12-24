'''
Transpose

We can generate the transposition of an array using the tool 
numpy.transpose. It will not affect the original array, but it will 
create a new array.

Flatten

The tool flatten creates a copy of the input array flattened to one 
dimension.

Task

You are given a NXM  integer array matrix with space separated elements 
(N = rows and M = columns).
Your task is to print the transpose and flatten results.
'''

import numpy as np

if __name__=='__main__':
    n, m = input().split()
    my_array = np.array([list(map(int, input().split())) for _ in range(int(n))])
    print(np.transpose(my_array))
    print(my_array.flatten())