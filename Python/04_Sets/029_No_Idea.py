'''
There is an array of `n` integers. There are also 2 disjoint sets, 
`A` and `B`, each containing `m` integers. You like all the integers in set
`A` and dislike all the integers in set `B`. Your initial happiness is 0.

For each `i` integer in the array, if `i in A`, you add 1 to your happiness.
If `i in B`, you add -1 to your happiness. Otherwise, your happiness does 
not change. Output your final happiness at the end.

Note: Since `A` and `B` are sets, they have no repeated elements. However, 
the array might contain duplicate elements.
'''

if __name__ == '__main__':
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    set_1 = set(map(int, input().split()))
    set_2 = set(map(int, input().split()))

    print(sum([(i in set_1) - (i in set_2) for i in array]))
    
    # A = len(array.intersection(set_1))
    # B = len(array.intersection(set_2))

    # happiness_score = A - B

    # print(A, B, happiness_score)