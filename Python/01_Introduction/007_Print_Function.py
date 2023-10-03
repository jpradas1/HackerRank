'''
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:
123...n

Note that "..." represents the consecutive values in between.

Example:
n = 5

Print the string '12345'.
'''

def consecutive_values(n):
   if n == 0:
       return ''
   else:
       return str(consecutive_values(n-1)) + str(n)

if __name__ == '__main__':
    n = int(input())
    print(consecutive_values(n))