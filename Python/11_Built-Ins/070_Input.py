'''
You are given a polynomial `P` of a single indeterminate (or variable), `x`.
You are also given the values of `x` and `k`. Your task is to verify 
if `P(x)=k`.

Constraints
All coefficients of polynomial `P` are integers.
`x` and `y` are also integers.
'''

if __name__=='__main__':
    x, k = map(int, input().split())
    print(eval(input()) == k)
