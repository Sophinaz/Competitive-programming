class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for j in range(len(grid))]
        direction = [[0,1], [1,0], [-1,0], [0,-1]]
        
        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 1
        que = deque()
        later = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    que.append((i,j))
                    later.append((i,j))
                    visited[i][j] = True
        if not later or len(later) == len(grid) ** 2: return -1
        level = 0
        while que:
            for _ in range(len(que)):
                row, col = que.popleft()
                for r, c in direction:
                    new_row = row + r
                    new_col = col + c
                    if valid(new_row, new_col) and not visited[new_row][new_col]:
                        que.append((new_row, new_col))
                        visited[new_row][new_col] = True
            level += 1
        result = float('inf')
        for r, c in later:
            result = min(result, abs(row-r) + abs(col-c))
        return result