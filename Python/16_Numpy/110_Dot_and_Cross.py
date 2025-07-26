'''
dot
---

The dot tool returns the dot product of two arrays.

```
    import numpy

    A = numpy.array([ 1, 2 ])
    B = numpy.array([ 3, 4 ])

    print numpy.dot(A, B)       #Output : 11
```

cross
-----

The cross tool returns the cross product of two arrays.

```
    import numpy

    A = numpy.array([ 1, 2 ])
    B = numpy.array([ 3, 4 ])

    print numpy.cross(A, B)     #Output : -2
```

TASK
----

You are given two arrays `A` and `B`. Both have dimensions of `N`X`N`.
Your task is to compute their matrix product.
'''

if __name__ == '__main__':
    import numpy as np

    N = int(input())
    A = np.array([list(map(int, input().split())) for _ in range(N)])
    B = np.array([list(map(int, input().split())) for _ in range(N)])
    print(np.matmul(A, B))