'''
The provided code stub reads two integers, A and B, from STDIN.

Add logic to print two lines. The first line should contain 
the result of integer division, A//B. 
The second line should contain the result of float division,  A/B.

No rounding or formatting is necessary.
'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)