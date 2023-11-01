'''
start() & end()
These expressions return the indices of the start and end of the substring 
matched by the group.

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0


TASK
You are given a string `S`.
Your task is to find the indices of the start and end of string `k` in `S`.
'''
import re

if __name__=='__main__':
    S = input()
    k = input()

    result = []
    for item in re.finditer(r'(?=({}))'.format(k), S):
        result.append((item.start(), item.start()+len(k)-1))
    
    if result:
        for ii in result:
            print(ii)
    else:
        print((-1,-1))