'''
Consider the following:

-* A string, `s`, of length `n` where `s=c_0c_1..c_{n-1}`.
An integer, `k`.
We can split `s` into substrings of length `k` or lower, where each 
subtring, `t_i`, consists of a contiguous block of `k` or lower characters 
in `s`. Then, use each `t_i` to create string `u_i` such that:

-* The characters in `u_i` are a subsequence of the characters in `t_i`.
-* Any repeat occurrence of a character is removed from the string such 
   that each character in `u_i` occurs exactly once. In other words, if the 
   character at some index `j` in `t_i` occurs at a previous index 
   `<j` in `t_i`, then do not include the character in string `u_i`.

Given `s` and `k`, print `n//k` lines where each line `i` denotes string `u_i`.
'''

import textwrap as twt

def merge_the_tools(string, k):
    t_sequence = twt.wrap(text=string, width=k)
    u_sequence = []
    for tt in t_sequence:
        new_string = ''
        for x in tt:
            if x in new_string:
                continue
            else:
                new_string += x
        u_sequence.append(new_string)
    print('\n'.join(u_sequence))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)