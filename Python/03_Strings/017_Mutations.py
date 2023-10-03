'''
We have seen that lists are mutable (they can be changed),
and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

- One solution is to convert the string to a list and then change 
  the value.
Example:

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra

- Another approach is to slice the string and join it back.
Example:

>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra

%% TASK

Read a given string, change the character at a given index and then 
print the modified string.
'''

def mutate_string(string: str, position: int, character: str):
    new_str = list(string)
    new_str[position] = character
    new_str = ''.join(new_str)
    return new_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)