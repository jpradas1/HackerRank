'''
In this task, we would like for you to appreciate the usefulness of the 
groupby() function of itertools. To read more about this function, Check 
this out:
    https://docs.python.org/2/library/itertools.html#itertools.groupby

You are given a string `S`. Suppose a character 'c' occurs consecutively `X`
times in the string. Replace these consecutive occurrences of the character
'c' with `(X,c)` in the string.
'''

from itertools import groupby

if __name__=='__main__':
    chain = input()
    print(*[(len(list(g)), int(k)) for k, g in groupby(chain)])