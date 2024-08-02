grid = [[0,0,1],[1,0,1],[0,0,0]]

from itertools import pairwise

def func(grid):
  
    result = max((a,b) for a,b in pairwise(grid))
    
    return result


print(func(grid))



