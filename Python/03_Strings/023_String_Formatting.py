'''
Given an integer, `n`, print the following values for each 
integer `i` from 1 to `n`:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

-* Sample Input
17

-* Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
'''

def print_formatted(number: int):
    l = len(bin(number)) - 2
    for ii in range(1, number + 1):
        row = ' '.join(["{:>"+str(l)+ff+"}" for ff in 'doXb'])
        print(row.format(*[ii]*4))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)