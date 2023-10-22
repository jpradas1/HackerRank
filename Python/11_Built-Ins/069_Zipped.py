'''
zip([iterable, ...])

This function returns a list of tuples. The ith tuple contains the i_th 
element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list 
is truncated to the length of the shortest argument sequence.

Sample Code

>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]

TASK

The National University conducts an examination of `N` students in `X` 
subjects.
Your task is to compute the average scores of each student.
'''

if __name__=='__main__':
    N, X = map(int, input().split())
    sample = [list(map(float, input().split())) for _ in range(X)]
    
    ave = list(zip(*sample))
    ave = [sum(x)/X for x in ave]

    print(*ave, sep='\n')