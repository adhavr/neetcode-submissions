class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == "0":
                return
            grid[i][j] = "0"

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for k in range(len(grid)):
            for l in range(len(grid[0])):
                if grid[k][l] == "1":
                    dfs(k, l)
                    count += 1
        
        return count
