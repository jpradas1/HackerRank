'''
You are asked to ensure that the first and last names of people begin 
with a capital letter in their passports. 
For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s: str):
    lower_names = re.findall('\w+', s)
    upper_names = [x[0].upper()+x[1:] for x in lower_names]
    for ll, uu in zip(lower_names,upper_names):
        s = s.replace(ll, uu)
    return s

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = solve(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
