'''
Let's learn some new Python concepts! You have to generate a list of the 
first `N` fibonacci numbers, 0 being the first number. Then, apply the map 
function and a lambda expression to cube each fibonacci number and print 
the list.
'''

cube = lambda x: x**3

def fibonacci(n: int):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for _ in range(n-2):
        sequence.append(sum(sequence[-2:]))
    return sequence

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))