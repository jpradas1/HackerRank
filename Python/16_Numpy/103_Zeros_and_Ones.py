'''
zeros

The zeros tool returns a new array with a given shape and type filled 
with 0's.

ones

The ones tool returns a new array with a given shape and type filled 
with 1's.

TASK

You are given the shape of the array in the form of space-separated 
integers, each integer representing the size of different dimensions, 
your task is to print an array of the given shape and integer type using 
the tools numpy.zeros and numpy.ones.
'''

import numpy as np

if __name__=='__main__':
    shape = tuple(map(int, input().split()))
    print(np.zeros(shape=shape, dtype=int))
    print(np.ones(shape=shape, dtype=int))