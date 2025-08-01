'''
re.findall()
The expression `re.findall()` returns all the non-overlapping matches of 
patterns in a string as a list of strings.

>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']


re.finditer()
The expression `re.finditer()` returns an iterator yielding `MatchObject` 
instances over all non-overlapping matches for the re pattern in the string.

>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']


TASK
You are given a string `S`. It consists of alphanumeric characters, spaces 
and symbols(+,-).
Your task is to find all the substrings of `S` that contains  or more 
vowels.
Also, these substrings must lie in between  2consonants and should contain 
vowels only.
'''

import re

if __name__=='__main__':
    s = input()
    vowels = 'AEIOUaeiou'
    consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
    matches = re.findall(fr'((?<=[{consonants}])[{vowels}][{vowels}]+(?=[{consonants}]))', s)
    if matches:
        print('\n'.join(matches))
    else:
        print(-1)
