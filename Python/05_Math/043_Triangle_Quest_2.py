'''
You are given a positive integer `N`.
Your task is to print a palindromic triangle of size `N`.

For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321

You can't take more than two lines. The first line (a for-statement) is 
already written for you.
You have to complete the code using exactly one print statement.

Note:
Using anything related to strings will give a score of 0.
Using more than one for-statement will give a score of 0.
'''

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    # print(int(''.join([str(n) for n in range(1,i+1)]+[str(n) for n in range(1,i)][::-1])))
    # print(sum([n*(10**(i-n)) for n in range(i)])*10**(i-1)+sum([n*(10**(n-1)) for n in range(1,i+1)]))
    print (((10**i - 1)//9)**2)