import os

def makeCommits (days : int):
    if days < 1:

        return days * makeCommits(days - 1)
    
makeCommits(3)
