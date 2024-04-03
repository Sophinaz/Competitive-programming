class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def firstcell(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1: return i, j
        
        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1
        
        def dfs(grid, directions, row, col):
            nonlocal result
            visited[row][col] = True
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                
                if valid(new_row, new_col):
                    if not visited[new_row][new_col]:
                        dfs(grid, directions, new_row, new_col)
                else:
                    if grid[row][col] == 1:
                        result += 1

        r, c = firstcell(grid)
        dfs(grid, directions, r, c)
        return result

                
