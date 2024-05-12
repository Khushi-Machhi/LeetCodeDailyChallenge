# 2373. Largest Local Values in a Matrix

class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """

        l = len(grid)
        result = []

        for i in range(1,l-1):
            r = []
            for j in range(1,l-1):

                sub = [grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                             grid[i][j-1],   grid[i][j],   grid[i][j+1],
                             grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]]

                m = max(sub)
                r.append(m)
            result.append(r)

        return result



