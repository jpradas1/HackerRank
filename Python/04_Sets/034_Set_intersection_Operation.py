'''
The students of District College have subscriptions to English and French 
newspapers. Some students have subscribed only to English, some have 
subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to 
the English newspaper, one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to 
both newspapers.
'''

if __name__ == '__main__':
    n = int(input())
    N = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))

    # print(len(N & B))
    print(len(N.intersection(B)))