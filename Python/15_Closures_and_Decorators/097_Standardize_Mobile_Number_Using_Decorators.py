'''
Let's dive into decorators! You are given `N` mobile numbers. Sort them in 
ascending order then print them in the standard format shown below:

    +91 xxxxx xxxxx

The given mobile numbers may have `+91`, `91` or `0` written before the 
actual 10 digit number. Alternatively, there may not be any prefix at all.
'''

def wrapper(f):
    def fun(l):
        l = ['+91 ' + x[-10:] for x in l]
        l = [x.replace(x[-5:], f' {x[-5:]}') for x in l]
        print(*sorted(l), sep='\n')
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)