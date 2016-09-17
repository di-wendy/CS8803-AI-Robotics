# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
import numpy as np

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    visit_list = []
    visit_list.append(init)
    length = len(grid)
    width = len(grid[0])
    find = False
    grid[init[0]][init[1]]=cost
    
    while (visit_list != []):
        status = visit_list.pop()
        
        for move in delta:
            new_status = np.subtract(status,move)
            i = new_status[0]
            j = new_status[1]
            
            if np.array_equal(new_status,goal):
                find = True
                path = [grid[status[0]][status[1]],status[0],status[1]]
                break
            if (i in range(0,length))and (j in range(0,width)) and grid[i][j]==0:
                visit_list.append(new_status)
                grid[i][j]=grid[status[0]][status[1]]+cost
                
    if find == False:
        return 'fail'
    print grid
    return path

print search(grid,init,goal,cost)
