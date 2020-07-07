class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        tote = 0
        leng = len(grid)
        i = 0 
        while i < leng:
            lenc = len(grid[i])
            j = 0 
            while j < lenc:
                if grid[i][j] == 1:
                    ### top
                    if i == 0:
                        tote = tote + 1
                    else:
                        if i-1 > -1 and grid[i-1][j] == 0:
                            tote = tote + 1 
                    ### bottom
                    if i == leng-1:
                        tote = tote + 1
                    else:
                        if i+1 < leng and grid[i+1][j] == 0:
                            tote = tote + 1 
                    ### left
                    if j == 0:
                        tote = tote + 1
                    else:
                        if j-1 > -1 and grid[i][j-1] == 0:
                            tote = tote + 1 
                    ### right 
                    if j == len(grid[i])-1:
                        tote = tote + 1
                    else:
                        if j+1 < len(grid[i]) and grid[i][j+1] == 0:
                            tote = tote + 1
                j = j + 1 
            i = i + 1 
        return tote 