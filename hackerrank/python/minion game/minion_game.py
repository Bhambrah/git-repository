# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:02:57 2018

@author: Sumeet Bhambrah

Hackerrank | Python | Strings | Minion Game

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string S.
For Example:
String = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 
Your task is to determine the winner of the game and their score.

Input Format
A single line of input containing the string S. 
Note: The string S will contain only uppercase letters: A-Z.

Constraints:
0 < len(S) <= 10^6

Output Format
Print one line: the name of the winner and their score separated by a space. 
If the game is a draw, print Draw.

"""
def minion_game(string):
    kevin = 0
    stuart = 0
    substrings = [string[i:j+1] for i in range(len(string)) for j in range(i,len(string))]
    for str in substrings:
        if(str[0] in ('A','E','I','O','U')):
            kevin+=1
        else:
            stuart+=1
    if kevin == stuart:
        print("Draw")
    else:
        print("Stuart %d" % stuart if stuart>kevin else "Kevin %d" % kevin)

if __name__ == '__main__':
    s = input()
    minion_game(s)