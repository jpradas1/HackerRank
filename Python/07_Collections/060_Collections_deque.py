'''
collections.deque()
A deque is a double-ended queue. It can be used to add or remove elements 
from both ends.

Deques support thread safe, memory efficient appends and pops from either 
side of the deque with approximately the same `O(1)` performance in either 
direction.

Click on the link to learn more about deque() methods.
    https://docs.python.org/2/library/collections.html#deque-objects

Click on the link to learn more about various approaches to working with 
deques: Deque Recipes.
    https://docs.python.org/2.7/library/collections.html#deque-recipes

TASK

Perform append, pop, popleft and appendleft methods on an empty deque .
'''

from collections import deque

if __name__ == '__main__':
    N = int(input())
    deq = deque()

    for _ in range(N):
        command, *line = input().split()
        keys = list(map(int, line))
        executed = {'command': command, 'keys': keys}

        match executed:
            case {'command':'append'}:
                deq.append(*executed['keys'])
            case {'command':'appendleft'}:
                deq.appendleft(*executed['keys'])
            case {'command':'pop'}:
                deq.pop()
            case {'command':'popleft'}:
                deq.popleft()

    print(*deq)