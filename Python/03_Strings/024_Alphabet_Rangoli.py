'''
You are given an integer, `N`. Your task is to print an alphabet rangoli 
of size `N`. (Rangoli is a form of Indian folk art based on creation of 
patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

def print_rangoli(size):
    letter = lambda x: chr(ord('A')+x).lower()

    # Middle pattern
    middle_patten = '-'.join([letter(ii) for ii in range(size)])
    middle_patten = middle_patten[1:][::-1] + middle_patten

    # Upper and lower pattern
    patterns = []
    aux_pattern = middle_patten
    for _ in range(size-1)   :
        delete_pattern = aux_pattern[(size-1)*2-1:(size-1)*2+3]
        aux_pattern = aux_pattern.replace(delete_pattern, '').center(len(middle_patten), '-')
        patterns.append(aux_pattern)

    for upper in patterns[::-1]:
        print(upper)
    print(middle_patten)
    for lower in patterns:
        print(lower)
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)