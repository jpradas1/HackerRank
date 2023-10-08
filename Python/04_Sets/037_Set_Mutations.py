'''
You are given a set `A` and `N` number of other sets. These `N` number of 
sets have to perform some specific mutation operations on set .

Your task is to execute those operations and print the sum of elements 
from set `A`.

Input Format

The first line contains the number of elements in set `A`.
The second line contains the space separated list of elements in set `A`.
The third line contains integer `N`, the number of other sets.
The next `2*N` lines are divided into `N` parts containing two lines each.
The first line of each part contains the space separated entries of the 
operation name and the length of the other set.
The second line of each part contains space separated list of elements in 
the other set.
'''

def verify_size(size: int, array: set | list):
    if len(array) != size:
        raise ValueError
    else:
        return None

if __name__ == '__main__':
    a = int(input())
    A = set(map(int, input().split()))
    N = int(input())
    command, size = '', -1

    for ii in range(2*N):
        if ii%2 == 0:
            command, size = input().split()
            continue
        else:
            update = set(map(int, input().split()))
            verify_size(int(size), update)
            executed = {'command': command}

            match executed:
                case {'command':'update'}:
                    A.update(update)
                case {'command':'intersection_update'}:
                    A.intersection_update(update)
                case {'command':'difference_update'}:
                    A.difference_update(update)
                case {'command':'symmetric_difference_update'}:
                    A.symmetric_difference_update(update)

    print(sum(A))