'''
Mr. Vincent works in a door mat manufacturing company. One day, 
he designed a new door mat with the following specifications:

Mat size must be `N`X`M`. (`N` is an odd natural number, and `M` is 3 times `N`.)
The design should have 'WELCOME' written in the center.
The design pattern should only use `|`, `.` and `-` characters.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
'''

if __name__ == '__main__':
    N, m = list(map(int, input().split()))
    M = 3 * N
    
    if N%2 == 0:
        raise ValueError
    
    pattern = '.|.'

    # Upper pattern
    for ii in range(N//2):
        print((pattern*(2*ii+1)).center(M, '-'))

    # Middle message
    print('WELCOME'.center(M, '-'))

    # Lower pattern
    for ii in range(N//2)[::-1]:
        print((pattern*(2*ii+1)).center(M, '-'))