'''
group()
A `group()` expression returns one or more subgroups of the match.

>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.group(0)       # The entire match 
'username@hackerrank.com'
>>> m.group(1)       # The first parenthesized subgroup.
'username'
>>> m.group(2)       # The second parenthesized subgroup.
'hackerrank'
>>> m.group(3)       # The third parenthesized subgroup.
'com'
>>> m.group(1,2,3)   # Multiple arguments give us a tuple.
('username', 'hackerrank', 'com')


groups()
A `groups()` expression returns a tuple containing all the subgroups of the 
match.

>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.groups()
('username', 'hackerrank', 'com')


groupdict()
A `groupdict()` expression returns a dictionary containing all the named 
subgroups of the match, keyed by the subgroup name.

>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}

TASK

You are given a string `S`.
Your task is to find the first occurrence of an alphanumeric character in `S` 
(read from left to right) that has consecutive repetitions.
'''
import re

if __name__=='__main__':
    S = re.search(r'([0-9a-zA-Z])\1+', input())

    try:
        print(S.group(0)[0])
    except:
        print(-1)