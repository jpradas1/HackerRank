'''
**    .remove(x)    **
This operation removes element `x` from the set.
If element `x` does not exist, it raises a `KeyError`.
The .remove(x) operation returns `None`.

**    .discard(x)    **
This operation also removes element `x` from the set.
If element `x` does not exist, it does not raise a `KeyError`.
The .discard(x) operation returns `None`.

**    .pop()    **
This operation removes and return an arbitrary element from the set.
If there are no elements to remove, it raises a `KeyError`.

TASK

You have a non-empty set , and you have to execute  commands given in  lines.

The commands will be pop, remove and discard.

%% Input Format

The first line contains integer `n`, the number of elements in the set `s`.
The second line contains `n` space separated elements of set `s`.
All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer `N`, the number of commands.
The next `N` lines contains either pop, remove and/or discard commands 
followed by their associated value.

%% Output Format

Print the sum of the elements of set `s` on a single line.
'''

n = int(input())
s = set(map(int, input().split()))
N = int(input())

if len(list(s)) != n:
    raise ValueError

for _ in range(N):
    command = list(map(str, input().split()))
    
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))
    
print(sum(list(s)))