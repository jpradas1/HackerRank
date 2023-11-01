'''
The `re.sub()` tool (sub stands for substitution) evaluates a pattern and, 
for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in 
different ways.
The re.sub() method returns the modified string as an output.

Learn more about `re.sub()`.

Transformation of Strings

>>> import re

#Squaring numbers
>>> def square(match):
        number = int(match.group(0))
        return str(number**2)

>>> print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")

Output
>>> 1 4 9 16 25 36 49 64 81

TASK

You are given a text of `N` lines. The text contains `&&` and `||` symbols.
Your task is to modify those symbols to the following:

&& → and
|| → or
'''
import re

if __name__=='__main__':
    N = int(input())
    text = '\n'.join([input() for _ in range(N)])

    new_text = re.sub(r'((?<=\s)\|\|(?=\s))', 'or', text)
    new_text = re.sub(r'((?<=\s)&&(?=\s))', 'and', new_text)

    print(new_text)