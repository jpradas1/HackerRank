'''
Python has built-in string validation methods for basic data. 
It can check if a string is composed of alphabetical characters, 
alphanumeric characters, digits, etc.

- str.isalnum()
This method checks if all the characters of a string are alphanumeric 
(a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False

- str.isalpha()
This method checks if all the characters of a string are alphabetical 
(a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False

- str.isdigit()
This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False

- str.islower()
This method checks if all the characters of a string are lowercase 
characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False

- str.isupper()
This method checks if all the characters of a string are uppercase 
characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False

%% TASK

You are given a string `S`.
Your task is to find out if the string `S` contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters.
'''

if __name__ == '__main__':
    s = input()

    print(any(x.isalnum() for x in s))
    print(any(x.isalpha() for x in s))
    print(any(x.isdigit() for x in s))
    print(any(x.islower() for x in s))
    print(any(x.isupper() for x in s))