'''
If we want to add a single element to an existing set, we can use 
the .add() operation. It adds the element to the set and returns 'None'.

TASK

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the 
total number of distinct country stamps in her collection. She asked for 
your help. You pick the stamps one by one from a stack of `N` country stamps.

Find the total number of distinct country stamps.
'''

if __name__ == '__main__':
    number = int(input())
    country_set = set()
    for _ in range(number):
        country_set.add(input())
    
    print(len(country_set))