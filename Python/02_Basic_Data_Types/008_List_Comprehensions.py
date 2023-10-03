'''
Let's learn about list comprehensions! You are given three integers `x`,
`y` and `z` representing the dimensions of a cuboid along with an 
integer `n`.
Print a list of all possible coordinates given by `(i, j, k)` on a 3D grid
where the sum of `i+j+k` is not equal to `n`.

Here, `0<=i<=x`; `0<=j<=y`; `0<=k<=z`.

Please use list comprehensions rather than multiple loops, as a learning 
exercise.
'''

def coordinates_ranges(x, y, z):
    i = range(x+1)
    j = range(y+1)
    k = range(z+1)
    return i, j, k

def permutations(x, y, z, n):
    i, j, k = coordinates_ranges(x, y, z)
    perm = [[ii, jj, kk] for ii in i for jj in j for kk in k]
    perm = [x for x in perm if sum(x) != n]
    return perm

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(permutations(x, y, z, n))