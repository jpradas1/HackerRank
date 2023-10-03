'''
In this challenge, the user enters a string and a substring. You have 
to print the number of times that the substring occurs in the given string. 

String traversal will take place from left to right, not from right to 
left.

NOTE: String letters are case-sensitive.
'''

def count_substring(string: str, sub_string: str):
    stopcase = len(sub_string)-1
    pattern = [ss + string[ii+1:ii+len(sub_string)] for ii, ss in enumerate(string[:-stopcase])]
    pattern = [x for x in pattern if x == sub_string]
    return len(pattern)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)