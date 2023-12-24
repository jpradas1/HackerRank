'''
Concatenate

Two or more arrays can be concatenated together using the concatenate 
function with a tuple of the arrays to be joined:

    import numpy

    array_1 = numpy.array([1,2,3])
    array_2 = numpy.array([4,5,6])
    array_3 = numpy.array([7,8,9])

    print numpy.concatenate((array_1, array_2, array_3))    

    #Output
    [1 2 3 4 5 6 7 8 9]

If an array has more than one dimension, it is possible to specify the axis 
along which multiple arrays are concatenated. By default, it is along the 
first dimension.

    import numpy

    array_1 = numpy.array([[1,2,3],[0,0,0]])
    array_2 = numpy.array([[0,0,0],[7,8,9]])

    print numpy.concatenate((array_1, array_2), axis = 1)   

    #Output
    [[1 2 3 0 0 0]
    [0 0 0 7 8 9]]    

TASK

You are given two integer arrays of size NXP and MXP (N & M are rows, and P
is the column). Your task is to concatenate the arrays along axis 0.
'''

import numpy as np

if __name__=='__main__':
    n, m, p = map(int, input().split())
    n_p, m_p = [], []
    for _ in range(n):
        n_p.append(list(map(int, input().split())))
    for _ in range(m):
        m_p.append(list(map(int, input().split())))

    print(np.concatenate(
        (np.array(n_p), np.array(m_p)),
        axis=0
    ))