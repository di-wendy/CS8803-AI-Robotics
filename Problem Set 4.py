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
    init_grid = init + [1]
    visit_list.append(init_grid)
    grid[init[0]][init[1]]=cost
    
    Find = False
    
    while(visit_list != []):
        
        visit_list = sorted(visit_list,key = lambda student:student[2],reverse = True)
        c_s = visit_list.pop()
        if c_s[0]==goal[0] and c_s[1]==goal[1]:
            Find = True
            path = [c_s[2]-1,c_s[0],c_s[1]]
            break
        
        for move in delta:
            i = c_s[0]-move[0]
            j = c_s[1]-move[1]
            if (i in range(0,len(grid))) and (j in range(0,len(grid[0]))):
                if grid[i][j] == 0:
                    n_s = [i,j]
                    grid[i][j] = grid[c_s[0]][c_s[1]]+cost
                    visit_list.append([i,j,grid[i][j]])
    
    if Find == False:
        return 'fail'

    
    return path

print search(grid,init,goal,cost)
