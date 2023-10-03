'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given n scores. 
Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array A[]
of n integers each separated by a space.
'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    if len(arr) != n:
        raise ValueError
    
    arr = sorted(set(arr))
    runner_up = arr[-2]
    print(runner_up)