'''
You are given a string, and you have to validate whether it's a valid Roman 
numeral. If it is valid, print True. Otherwise, print False. Try to create 
a regular expression for a valid Roman numeral.
'''
import re

if __name__=='__main__':
    regex_pattern = r"^(C?M{0,3}(?>CM)?D?C{0,3}(?>CD)?X?C?L?X{0,3}V?I{0,3}V?X?)$"
    print(str(bool(re.match(regex_pattern, input()))))