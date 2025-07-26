'''
mean
----

The `mean` tool computes the arithmetic mean along the specified axis.

```
    import numpy

    my_array = numpy.array([ [1, 2], [3, 4] ])

    print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
    print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
    print numpy.mean(my_array, axis = None)     #Output : 2.5
    print numpy.mean(my_array)                  #Output : 2.5
```

By default, the axis is None. Therefore, it computes the mean of the flattened
array.

var
---

The `var` tool computes the arithmetic variance along the specified axis.

```
    import numpy

    my_array = numpy.array([ [1, 2], [3, 4] ])

    print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
    print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
    print numpy.var(my_array, axis = None)      #Output : 1.25
    print numpy.var(my_array)                   #Output : 1.25
```
By default, the axis is None. Therefore, it computes the variance of the
flattened array.

std
---

The `std` tool computes the arithmetic standard deviation along the specified
axis.

```
    import numpy

    my_array = numpy.array([ [1, 2], [3, 4] ])

    print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
    print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
    print numpy.std(my_array, axis = None)      #Output : 1.11803398875
    print numpy.std(my_array)                   #Output : 1.11803398875
```

By default, the axis is None. Therefore, it computes the standard deviation of
the flattened array.

TASK
----

You are given a 2-D array of size `N`X`M`.
Your task is to find:

1. The mean along axis `1`
2. The var along axis `0`
3. The std along axis `None`
'''

if __name__ == '__main__':
    import numpy as np

    N, M = map(int, input().split())
    matrix = np.array([input().split() for _ in range(N)], dtype=int)
    print(np.mean(matrix, axis=1))
    print(np.var(matrix, axis=0))
    print(np.std(matrix, axis=None).round(11))