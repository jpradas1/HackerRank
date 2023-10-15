'''
collections.namedtuple()

Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing 
members of a tuple.

TASK

Dr. John Wesley has a spreadsheet containing a list of student's `ID`,
`MARKS`, `CLASS` and `NAME`.

Your task is to help Dr. Wesley calculate the average marks of the students.
'''

from collections import namedtuple

if __name__=='__main__':
    N, Student = int(input()), namedtuple('Student', input())
    result = list(int(Student(*list(map(str, input().split()))).MARKS) for _ in range(N))
    print(f'{sum(result)/N:.2f}')