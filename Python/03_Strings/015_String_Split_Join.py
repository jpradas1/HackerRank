'''
In Python, a string can be split on a delimiter.

Example:

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']

Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 

%% Task
You are given a string. Split the string on a " " (space) delimiter and 
join using a - hyphen.
'''

def split_and_join(line):
    new_line = line.split(' ')
    new_line = '-'.join(new_line)
    return new_line
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)