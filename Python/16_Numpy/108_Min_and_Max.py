'''
min
---

The tool `min` returns the minimum value along a given axis.

```
    import numpy

    my_array = numpy.array([[2, 5], 
                            [3, 7],
                            [1, 3],
                            [4, 0]])

    print numpy.min(my_array, axis = 0)         #Output : [1 0]
    print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
    print numpy.min(my_array, axis = None)      #Output : 0
    print numpy.min(my_array)                   #Output : 0
```

By default, the axis value is None. Therefore, it finds the minimum over all
the dimensions of the input array.

max
---

The tool `max` returns the maximum value along a given axis.

```
    import numpy

    my_array = numpy.array([[2, 5], 
                            [3, 7],
                            [1, 3],
                            [4, 0]])

    print numpy.max(my_array, axis = 0)         #Output : [4 7]
    print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
    print numpy.max(my_array, axis = None)      #Output : 7
    print numpy.max(my_array)                   #Output : 7
```

By default, the axis value is None. Therefore, it finds the maximum over all
the dimensions of the input array.

TASK
----

You are given a 2-D array with dimensions `N` X `M`.
Your task is to perform the min function over axis `1` and then find the max of
that.
'''

if __name__ == '__main__':
    import numpy as np

    N, M = map(int, input().split())
    matrix = np.array([list(map(int, input().split())) for _ in range(N)])
    result = np.max(np.min(matrix, axis=1))
    print(result)