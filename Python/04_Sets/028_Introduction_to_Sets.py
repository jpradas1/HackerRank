'''
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will 
appear in an arbitrary order.

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. 
One day, she asked her student Mickey to compute the average of all 
the plants with distinct heights in her greenhouse.
'''

def average(array: list):
    new_array = list(set(array))
    ave = sum(new_array)/len(new_array)
    return round(ave,3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)