'''
Neo has a complex matrix script. The matrix script is a `N`X`M` grid of 
strings. It consists of alphanumeric characters, spaces and symbols 
(!,@,#,$,%,&).


To decode the script, Neo needs to read each column and select only the 
alphanumeric characters and connect them. Neo reads the column from top to 
bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the 
decoded script, then Neo replaces them with a single space '' for better 
readability.

Neo feels that there is no need to use 'if' conditions for decoding.    
'''

import re

def cleansing(string: str) -> str:
    s = ''.join(re.findall(r'([0-9A-Za-z]+.*[0-9A-Za-z]+)', string))
    matches = re.findall(r'([0-9A-Za-z]*)([\W_]*)', s)

    new_string = []
    for x in matches:
        new_string.append(x[0])
    new_string = ' '.join(new_string[:-1])
    new_string = string.replace(s, new_string)
    return new_string

def tranposition(matrix: list, m: int) -> str:
    string = ''
    for ii in range(m):
        string +=  ''.join([x[ii] for x in matrix])
    return string

if __name__=='__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    string = tranposition(matrix, m)
    print(string)
    print(cleansing(string))
