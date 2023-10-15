'''
collections.Counter()

A counter is a container that stores elements as dictionary keys, and their 
counts are stored as dictionary values.

TASK

Raghu is a shoe shop owner. His shop has `X` number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are `N` number of customers who are willing to pay `x` amount of 
money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains `X`, the number of shoes.
The second line contains the space separated list of all the shoe sizes in 
the shop.
The third line contains `N`, the number of customers.
The next `N` lines contain the space separated values of the 'shoe size' 
desired by the customer and `x_i`, the price of the shoe.
'''

from collections import Counter

if __name__=='__main__':
    X = int(input())
    sizes = list(map(int, input().split()))

    counter_sizes = Counter(sizes)
    earnings = 0

    for _ in range(int(input())):
        size, price = map(int, input().split())
        if counter_sizes[size] > 0:
            earnings += price
            counter_sizes[size] -= 1
    
    print(earnings)