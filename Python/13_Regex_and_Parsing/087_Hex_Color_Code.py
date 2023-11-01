'''
CSS colors are defined using a hexadecimal (HEX) notation for the 
combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have  or  digits.
■ Each digit is in the range of 0 to F.
■ A-F letters can be lower case. (a,b,c,d,e and f are also valid digits).

Examples

Valid Hex Color Codes
#FFF 
#025 
#F0A1FB 

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff

You are given `N` lines of CSS code. Your task is to print all valid Hex 
Color Codes, in order of their occurrence from top to bottom.
'''
import re

if __name__=='__main__':
    css = '\n'.join([input() for _ in range(int(input()))])
    print('\n'.join(re.findall('#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?(?=[^ \n])', css)))