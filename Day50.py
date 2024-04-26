# 1289. Minimum Falling Path Sum II
class Solution(object):
    def minFallingPathSum(self, grid):
        n = len(grid)
        
        for i in range(1, n):
            minval = float('inf')
            secMinVal = float('inf')
            for j in range(n):
                if grid[i-1][j] < minval:
                    secMinVal = minval
                    minval = grid[i-1][j]
                elif grid[i-1][j] < secMinVal:
                    secMinVal = grid[i-1][j]
            
            for j in range(n):
                if grid[i-1][j] == minval:
                    grid[i][j] += secMinVal
                else:
                    grid[i][j] += minval
        
        return min(grid[-1])
