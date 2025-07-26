'''
inner
-----

The inner tool returns the inner product of two arrays.

```
    import numpy

    A = numpy.array([0, 1])
    B = numpy.array([3, 4])

    print numpy.inner(A, B)     #Output : 4
```

outer
-----

The outer tool returns the outer product of two arrays.

```
    import numpy

    A = numpy.array([0, 1])
    B = numpy.array([3, 4])

    print numpy.outer(A, B)     #Output : [[0 0]
                                #          [3 4]]
```

TASK
----

You are given two arrays: `A` and `B`.
Your task is to compute their inner and outer product.
'''

if __name__ == '__main__':
    import numpy as np
    A = np.array(list(map(int, input().split())), int)
    B = np.array(list(map(int, input().split())), int)
    print(np.inner(A, B))
    print(np.outer(A, B))
    