'''
You are given a string `S`.
Your task is to find out whether `S` is a valid regex or not.

Compile with pypy3
'''

import re

if __name__=='__main__':
    T = int(input())

    for _ in range(T):
        try:
            re.compile(input())
            print(True)
        except Exception:
            print(False)