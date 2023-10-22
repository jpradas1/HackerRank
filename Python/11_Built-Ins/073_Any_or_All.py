'''
any()
This expression returns `True` if any element of the iterable is true.
If the iterable is empty, it will return `False`.

all()
This expression returns True if all of the elements of the iterable are 
true. If the iterable is empty, it will return `True`.

TASK

You are given a space separated list of integers. If all the integers are 
positive, then you need to check if any integer is a palindromic integer.
'''

if __name__=='__main__':
    N = int(input())
    sample = list(map(int, input().split()))

    if all(x>0 for x in sample):
        if any(str(x)==str(x)[::-1] for x in sample):
            print(True)
        else:
            print(False)
    else:
        print(False)