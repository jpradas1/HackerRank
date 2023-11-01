'''
Let's dive into the interesting topic of regular expressions! You are 
given some input, and you are required to check whether they are valid 
mobile numbers.

A valid mobile number is a ten digit number starting with a 7, 8 or 9.
'''
import re

if __name__=='__main__':
    for _ in range(int(input())):
        m = re.findall(r'^([987]\d{9})$', input())
        if m:
            print('YES')
        else:
            print('NO')
