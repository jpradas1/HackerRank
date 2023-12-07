'''
A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
'''
import re

def consecutive(ccn: str, win: int):
    for ii in range(len(ccn[:-win])):
        if len(set(ccn[ii:ii+win])) == 1:
            return True
    return False

def Validating_CCN(ccn: str):
    invalid = 'Invalid'
    if ccn[0] not in ['4', '5', '6']:
        return invalid
    elif len(re.findall('\d', ccn)) != 16:
        return invalid
    elif re.findall(r'[^\d\-]', ccn):
        return invalid
    elif len(re.split(r'\-', ccn)) not in [1, 4]:
        return invalid
    elif list(set(len(x) for x in re.split(r'\-', ccn)))[0] not in [4, len(ccn)]:
        return invalid
    elif consecutive(ccn=''.join(re.split('-', ccn)), win=4):
        return invalid

    return 'Valid'

if __name__=='__main__':
    CCN = [input() for _ in range(int(input()))]
    for x in CCN:
        print(Validating_CCN(x))