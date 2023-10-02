'''
Given an integer, N , perform the following conditional actions:

If N is odd, print Weird
If N is even and in the inclusive range of 2 to 5, print Not Weird
If N is even and in the inclusive range of 6 to 20, print Weird
If N is even and greater than 20, print Not Weird
'''

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 0:
        if n >= 2 and n < 5:
            print('Not Weird')
        elif n >= 5 and n <= 20:
            print('Weird')
        else:
            print('Not Weird') 
    else:
        print('Weird')