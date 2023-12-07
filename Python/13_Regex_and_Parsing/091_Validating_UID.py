'''
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each 
of its employees.
The company has assigned you the task of validating all the randomly 
generated UIDs.

A valid UID must follow the rules below:

- It must contain at least 2 uppercase English alphabet characters.
- It must contain at least 3 digits (0-9).
- It should only contain alphanumeric characters (a-z, A-Z & 0-9).
No character should repeat.
- There must be exactly 10 characters in a valid UID.
'''
import re

def Validating_UID(uid: str):
    invalid = 'Invalid'
    if re.findall('[\W_]', uid):
        return invalid
    elif len(uid) != 10:
        return invalid
    elif len(re.findall('\d', uid)) < 3:
        return invalid
    elif len(re.findall('[A-Z]', uid)) < 2:
        return invalid
    elif len(uid) != len(set(uid)):
        return invalid
    return 'Valid'


if __name__=='__main__':
    for _ in range(int(input())):
        print(Validating_UID(input()))