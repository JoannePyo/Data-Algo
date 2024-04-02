'''
Assign Mice to Holes
There are N Mice and N holes are placed in a straight line. 
Each hole can accommodate only 1 mouse. 
A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x -1. 
Any of these moves consumes 1 minute. 
Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.

Input : positions of mice are:
            4 -4 2
        positions of holes are:
            4 0 5
Output :  4
'''

'''
def assignHole(mice, holes, m, h):
    

# Driver code 
mice = [ 4, -4, 2 ]
holes = [ 4, 0, 5 ]
m = len(mice) # Number of mouses
h = len(holes)  # Number of holes
minTime = assignHole(mice, holes, m, h)
print("The last mouse gets into the hole in time:", minTime)
'''

def assignHole(mice, holes, m, h):
    if m != h:
        return -1

    mice.sort()
    holes.sort()

    max_num = 0
    for i in range(m):
        if (max_num < (abs(mice[i]-(holes[i])))):
            max_num = (abs(mice[i]-(holes[i])))
        
    return max_num

# Driver code 
mice = [ 4, -4, 2 ]
holes = [ 4, 0, 5 ]
m = len(mice) # Number of mouses
h = len(holes)  # Number of holes
minTime = assignHole(mice, holes, m, h)
print("The last mouse gets into the hole in time:", minTime)