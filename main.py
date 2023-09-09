import os

def makeCommits (days : int):
    if days < 1:
        os.system('git push')
    else:
        dates = f"{days} days ago"
        
        os.system('git commit --date="'+ dates +'" -m "cupertino library"')

        return days * makeCommits(days - 1)
    
makeCommits(3)              