'''
The provided code stub reads and integer, n, from STDIN.
For all non-negative integers i<n, print i^2.
'''

if __name__ == '__main__':
    n = int(input())
    for ii in range(n):
        print(ii**2)