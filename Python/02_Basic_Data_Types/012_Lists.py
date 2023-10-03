'''
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer `e` at position `i`.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer `e`.
4. append e: Insert integer `e` at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of `n` followed by `n` lines 
of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding 
operation on your list.
'''

if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        command, *line = input().split()
        keys = list(map(int, line))
        executed = {'command': command, 'keys': keys}

        match executed:
            case {'command':'insert'}:
                lst.insert(*executed['keys'])
            case {'command':'print'}:
                print(lst)
            case {'command':'remove'}:
                lst.remove(*executed['keys'])
            case {'command':'append'}:
                lst.append(*executed['keys'])
            case {'command':'sort'}:
                lst = sorted(lst)
            case {'command':'pop'}:
                lst.pop()
            case {'command':'reverse'}:
                lst = lst[::-1]