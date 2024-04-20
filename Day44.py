# 1992. Find All Groups of Farmland

class Solution(object):
    def findFarmland(self, land):
        def dfs(row, col):
            land[row][col] = 0
            mx[0] = max(mx[0], row)
            mx_col[0] = max(mx_col[0], col)
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + i, col + j
    
                if 0 <= nr < m and 0 <= nc < n and land[nr][nc] == 1:
                    dfs(nr, nc)

        m, n = len(land), len(land[0])
        ans = []
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    mx, mx_col = [i], [j]
                    dfs(i, j)
                    ans.append([i, j, mx[0], mx_col[0]])

        return ans
