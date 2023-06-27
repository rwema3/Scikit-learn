import os

def makeCommits (days : int):

        return days * makeCommits(days - 1)
    
makeCommits(3)
