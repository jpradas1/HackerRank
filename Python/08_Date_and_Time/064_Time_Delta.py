'''
When users post an update on social media,such as a URL, image, status 
update etc., other users in their network are able to view this new post 
on their news feed. Users can also see exactly when the post was published, 
i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, 
this can be confusing. You are given two timestamps of one such post that 
a user can see on his newsfeed in the following format:

    Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute 
difference (in seconds) between them.
'''
#!/bin/python3

import os
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    date_names = ['day', 'month', 'year', 'hour', 'minute', 'second']

    t1 = [y for x in t1.split(' ')[1:] for y in x.split(':')]
    t2 = [y for x in t2.split(' ')[1:] for y in x.split(':')]

    tz1, tz2 = t1[-1], t2[-1]
    months = {'Jan': 1, 'Feb':2, 'Mar': 3, 'Apr': 4, 'May': 5, 
              'Jun': 6, 'Jul':7, 'Aug': 8, 'Sep': 9,
              'Oct': 10, 'Nov': 11, 'Dec': 12}
    
    t1[1] = months[t1[1]]
    t2[1] = months[t2[1]]
    t1, t2 = [int(x) for x in t1[:-1]], [int(x) for x in t2[:-1]]

    t1 = {k: v for k, v in zip(date_names, t1)}
    t2 = {k: v for k, v in zip(date_names, t2)}

    t1, t2 = datetime(**t1), datetime(**t2)
    tz1 = int(tz1[:-2])*3600 + int(tz1[-2:])*60
    tz2 = int(tz2[:-2])*3600 + int(tz2[-2:])*60
    delta = abs(int((t1-t2).total_seconds()) - (tz1 - tz2))

    print(delta)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)

        # fptr.write(delta + '\n')

    # fptr.close()