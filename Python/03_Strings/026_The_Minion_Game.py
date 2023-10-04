'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, `S`.
Both players have to make substrings using the letters of the string `S`.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in 
the string `S`.

For Example:
String `S`= BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Prints
string: the winner's name and score, separated by a space on one line, 
or Draw if there is no winner
'''
def minion_game(string: str):
    vowels = 'AEIOUaeiou'
    Stuart_score, Kevin_score = 0, 0
    length = len(string)
    for ii in range(length):
        score = length - ii
        if string[ii] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
    if Stuart_score == Kevin_score:
        print('Draw')
    elif Stuart_score > Kevin_score:
        print('Stuart {}'.format(Stuart_score))
    else:
        print('Kevin {}'.format(Kevin_score))

if __name__ == '__main__':
    s = input()
    minion_game(s)