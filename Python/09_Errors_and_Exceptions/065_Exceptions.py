'''
Exceptions
    https://docs.python.org/3/tutorial/errors.html

Errors detected during execution are called exceptions.

Examples:

ZeroDivisionError
This error is raised when the second argument of a division or modulo 
operation is zero.

>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero


ValueError
This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'

TASK

You are given two values `a` and `b`.
Perform integer division and print `a/b`.
'''

if __name__=='__main__':
    for _ in range(int(input())):
        a, b = map(str,input().split())
        try:
            print(int(a)//int(b))
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as e:
            print("Error Code:",e)
