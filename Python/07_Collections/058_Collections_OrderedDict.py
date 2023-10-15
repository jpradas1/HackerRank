'''
collections.OrderedDict

An OrderedDict is a dictionary that remembers the order of the keys that 
were inserted first. If a new entry overwrites an existing entry, the 
original insertion position is left unchanged.

TASK

You are the manager of a supermarket.
You have a list of `N` items together with their prices that consumers 
bought on a particular day.
Your task is to print each item_name and net_price in order of its first 
occurrence.
'''

from collections import OrderedDict

if __name__=='__main__':
    N = int(input())
    odct = OrderedDict()

    for _ in range(N):
        line = list(map(str,input().split()))
        name, price = ' '.join(line[:-1]), int(line[-1])
        if odct.get(name,''):
            odct[name] += price
        else:
            odct[name] = price

    for item in odct.items():
        print(*item)