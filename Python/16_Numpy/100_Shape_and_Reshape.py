'''
shape

The shape tool gives a tuple of array dimensions and can be used to change 
the dimensions of an array.

reshape

The reshape tool gives a new shape to an array without changing its data. 
It creates a new array and does not modify the original array itself.

Task

You are given a space separated list of nine integers. Your task is to 
convert this list into a 3X3 NumPy array.
'''

import numpy as np

if __name__=='__main__':
    my_array = np.array(list(map(int, input().split())))
    print(np.reshape(my_array, (3,3)))