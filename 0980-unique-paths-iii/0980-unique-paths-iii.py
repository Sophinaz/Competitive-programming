class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        count = 0

        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != -1

        for i in grid: 
            count += i.count(0)

        def dfs(row, col, walks):
            if grid[row][col] == 2:
                if len(walks) - 2 == count: 
                    return 1
                return 0

            res = 0
            for r, c in direction:
                new_row = row + r
                new_col = col + c
                if valid(new_row, new_col) and (new_row, new_col) not in walks:
                    walks.append((new_row, new_col))
                    res += dfs(new_row, new_col, walks)
                    walks.remove((new_row, new_col))
            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    a = [(i,j)]
                    return dfs(i, j, a)