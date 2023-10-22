'''
You are given a spreadsheet that contains a list of `N` athletes and their 
details (such as age, height, weight and so on). You are required to sort 
the data based on the Kth attribute and print the final resulting table. 
'''

if __name__=='__main__':
    n, m = map(int, input().split())

    sample = [list(map(int, input().split())) for _ in range(n)]
    ii = int(input())

    sample = {(v[ii],jj): v for jj, v in enumerate(sample)}
    for kk in sorted(sample.keys()):
        print(*sample[kk])