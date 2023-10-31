'''
You are given a string `N`.
Your task is to verify that `N` is a floating point number.

In this task, a valid float number must satisfy all of the following 
requirements:

1. Number can start with +, - or . symbol.
    For example:
    ✔ +4.50
    ✔ -1.0
    ✔ .5
    ✔ -.7
    ✔ +.4
    ✖ -+4.5

2. Number must contain at least  decimal value.
    For example:
    ✖ 12.
    ✔ 12.0  

3. Number must have exactly one . symbol.
4. Number must not give any exceptions when converted using `float(N)`.
'''
import re

if __name__=='__main__':
    sample = [input() for _ in range(int(input()))]

    for iterm in sample:
        print(bool(re.search('^[+-]?\d*\.\d+$', iterm)))