class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1], [1,0], [0,-1], [-1, 0]]
        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            grid[row][col] = "0"
            for r, c in directions:
                new_row = row + r
                new_col = col + c

                if valid(new_row, new_col) and grid[new_row][new_col] == "1":
                    dfs(new_row, new_col)


        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    result += 1

        return result