class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        visited = set()
        direction = [[0,1], [1,0], [0,-1], [-1,0]]
        count0 = 0
        
        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    que.append((row, col))
                    visited.add((row, col))
                elif grid[row][col] == 0:
                    count0 += 1

        count = -1
        if not que: count = 0
        
        while que:
            for _ in range(len(que)):
                row, col = que.popleft()

                for r, c in direction:
                    new_row = row + r
                    new_col = col + c
                    if valid(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                        que.append((new_row, new_col))
                        visited.add((new_row, new_col))
            count += 1

        if len(visited) == (len(grid) * len(grid[0])) - count0:
            return count
        return -1
