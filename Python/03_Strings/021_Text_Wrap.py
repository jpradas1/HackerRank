'''
You are given a string `S` and width `w`.
Your task is to wrap the string into a paragraph of width `w`.

-* Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

-* Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

import textwrap

def wrap(string: str, max_width: int):
    return '\n'.join(textwrap.wrap(text=string, width=max_width))
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)