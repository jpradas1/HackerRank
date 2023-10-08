'''
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an 
infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of `K` members per group 
  where `K` ≠ 1.

The Captain was given a separate room, and the rest were given one room 
per group.

Mr. Anant has an unordered list of randomly arranged room entries. 
The list consists of the room numbers for all of the tourists. 
The room numbers will appear `K` times per group except for the Captain's 
room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families 
is not known to you.
You only know the value of `K` and the room number list.
'''

def counter(array: list):
    values = list(set(array))
    count = [0] * len(values)
    for ii, y in enumerate(values):
        for x in array:
            if x == y:
                count[ii] += 1

    dct = {k: v for k, v in zip(count, values)}
    minn = min(dct.keys())
    return dct[minn]


if __name__ == '__main__':
    k = int(input())
    groups = sorted(map(int, input().split()))
    ii = 0
    length_set = len(set(groups[k*ii:k*(ii+1)]))
    length_array = len(groups[k*ii:k*(ii+1)])

    while(length_set == 1 and length_array == k):
        ii += 1
        length_array = len(groups[k*ii:k*(ii+1)])
        length_set = len(set(groups[k*ii:k*(ii+1)]))

    captain_room = groups[k*ii:k*(ii+1)]

    if len(captain_room) == 1:
        print(captain_room[0])
    elif len(set(captain_room)) != 1:
        print(counter(captain_room))