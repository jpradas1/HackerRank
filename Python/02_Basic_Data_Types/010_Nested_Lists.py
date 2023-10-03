'''
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having 
the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
'''

def second_lowest_value(record: list):
    second_lowest = sorted(list(set([x[1] for x in record])))[1]
    names = [x[0] for x in record if x[1]==second_lowest]
    return sorted(names)

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    for slv in second_lowest_value(records):
        print(slv)
    