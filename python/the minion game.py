"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string S.
"""


def minion_game(string):
    # your code goes here
    
    def stuart(string):
        vowels = ["A", "E", "I", "O", "U"]
        string = list(string)
        consonants = [(i, s) for i, s in enumerate(string) if s not in vowels]
        
        score = len(consonants)
        for i, c in consonants:
            score += len(string[i + 1:])
                
        return score
    
    def kevin(string):
        vowels = ["A", "E", "I", "O", "U"]
        string = list(string)
        vowels = [(i, s) for i, s in enumerate(string) if s in vowels]
        
        score = len(vowels)
        for i, c in vowels:
            score += len(string[i + 1:])
        
        return score
    
    if k > s:
        print("Kevin", k)
    elif k < s:
        print("Stuart", s)
    else:
        print("Draw")




def minion_game(string):
    # your code goes here
    s = 0
    k = 0
    length = len(string)
    vowels = ["A", "E", "I", "O", "U"]
    
    for i in range(length):
        if string[i] in vowels:
            k += length - i
        else:
            s += length - i
    
    if k > s:
        print("Kevin", k)
    elif k < s:
        print("Stuart", s)
    else:
        print("Draw")

