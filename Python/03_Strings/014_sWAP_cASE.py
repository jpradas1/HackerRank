'''
You are given a string and your task is to swap cases. In other words, 
convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
'''

def swap_case(s):
    new_s = ''
    for cc in s:
        if cc == cc.lower():
            new_s += cc.upper()
        else:
            new_s += cc.lower()
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)