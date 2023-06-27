import os

def makeCommits (days : int):
    if days < 1:
        os.system('git push')
    else:
        dates = f"{days} days ago"

        return days * makeCommits(days - 1)
    
makeCommits(3)
