'''
You are given a function `f(X)=X^2`. You are also given `K` lists. 
The `i_th` list consists of `N_i` elements.

You have to pick one element from each list so that the value from the 
equation below is maximized:

S = (f(X_1)+f(X_2)+...+f(X_k))%M

`X_i` denotes the element picked from the `i_th` list. Find the maximized 
value `S_max` obtained.

%  denotes the modulo operator.

Note that you need to take exactly one element from each list, not 
necessarily the largest element. You add the squares of the chosen elements 
and perform the modulo operation. The maximum value that you can obtain, 
will be the answer to the problem.
'''
import itertools as iter

if __name__=='__main__':
    K, M = map(int, input().split())
    Ns = []
    for _ in range(K):
        Ns.append([x for x in list(map(int, input().split()))[1:]])
    
    products = [x for x in iter.product(*Ns)]
    S = [sum(y**2 for y in x)%M for x in products]
    # S = map(lambda x: sum(i**2 for i in x)%M, iter.product(*Ns))
    print(max(S))