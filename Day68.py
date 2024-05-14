# 1219. Path with Maximum Gold
class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def backtrack(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0
            temp = grid[row][col]
            grid[row][col] = 0
            ans = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ans = max(ans, temp + backtrack(row + dr, col + dc))
            grid[row][col] = temp
            return ans
        
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, backtrack(i, j))
        return ans
        
