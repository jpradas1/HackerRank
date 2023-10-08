'''
You are given two sets, `A` and `B`.
Your job is to find whether set `A` is a subset of set `B`.

If set `A` is subset of set `B`, print True.
If set `A` is not a subset of set `B`, print False.
'''

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        na = int(input())
        A = set(map(int, input().split()))
        nb = int(input())
        B = set(map(int, input().split()))

        if len(A) != na or len(B) != nb:
            raise ValueError
        
        if A.intersection(B) == A:
            print(True)
        else:
            print(False)