'''
You are given  words. Some words may repeat. For each word, output its 
number of occurrences. The output order should correspond with the input 
order of appearance of the word. See the sample input/output for 
clarification.

Note: Each input line ends with a "\n" character.
'''
from collections import OrderedDict

if __name__=='__main__':
    n = int(input())
    odct = OrderedDict()
    
    for _ in range(n):
        word = input()
        if word in odct.keys():
            odct[word] += 1
        else:
            odct[word] = 1

    print(len(odct.keys()))
    print(*odct.values())