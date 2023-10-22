'''
You are given a string `S`.
`S` contains alphanumeric characters only.

Your task is to sort the string  in the following manner:

1. All sorted lowercase letters are ahead of uppercase letters.
2. All sorted uppercase letters are ahead of digits.
3. All sorted odd digits are ahead of sorted even digits.
'''
import re

if __name__=='__main__':
    word = input()

    lowercases = ''.join(sorted(re.findall('[a-z]',word)))
    uppercases = ''.join(sorted(re.findall('[A-Z]',word)))

    nums = re.findall('\d',word)
    
    odds = ''.join(sorted([x for x in nums if int(x)%2!=0]))
    even = ''.join(sorted([x for x in nums if int(x)%2==0]))

    print(f'{lowercases}{uppercases}{odds}{even}')