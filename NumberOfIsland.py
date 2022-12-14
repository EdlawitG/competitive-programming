class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        island = 0
        
        def dfs(grid,r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(grid,r+1,c)
            dfs(grid,r-1,c)
            dfs(grid,r,c+1)
            dfs(grid,r,c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(grid,r,c)
                    island +=1
        return island
